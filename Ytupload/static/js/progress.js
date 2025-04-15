// Socket.IO connection and progress tracking
let socket;
let currentVideoPath = null;

// Initialize Socket.IO connection
function initializeSocketConnection() {
    socket = io();
    
    // Connection events
    socket.on('connect', () => {
        console.log('Socket.IO connected');
    });
    
    socket.on('disconnect', () => {
        console.log('Socket.IO disconnected');
    });
    
    // Progress events
    socket.on('progress', handleProgress);
    socket.on('encoding_progress', handleEncodingProgress);
    socket.on('operation_update', handleOperationUpdate);
    socket.on('step_complete', handleStepComplete);
    socket.on('processing_complete', handleProcessingComplete);
    socket.on('processing_error', handleProcessingError);
}

// Handle progress updates
function handleProgress(data) {
    const progressBar = document.getElementById('progress-bar');
    const progressPercentage = document.getElementById('progress-percentage');
    
    const percent = Math.round(data.percent);
    progressBar.style.width = `${percent}%`;
    progressPercentage.textContent = `${percent}%`;
}

// Handle encoding progress updates
function handleEncodingProgress(data) {
    const encodingContainer = document.getElementById('encoding-progress-container');
    const encodingProgressBar = document.getElementById('encoding-progress-bar');
    const currentFrame = document.getElementById('current-frame');
    const totalFrames = document.getElementById('total-frames');
    const encodingPercentage = document.getElementById('encoding-percentage');
    
    encodingContainer.classList.remove('hidden');
    
    const percent = Math.round((data.current_frame / data.total_frames) * 100);
    encodingProgressBar.style.width = `${percent}%`;
    currentFrame.textContent = data.current_frame;
    totalFrames.textContent = data.total_frames;
    encodingPercentage.textContent = `${percent}%`;
}

// Handle operation updates
function handleOperationUpdate(data) {
    const currentOperation = document.getElementById('current-operation');
    currentOperation.textContent = data.message;
    
    // Add to log if available
    const processingLog = document.getElementById('processing-log');
    if (processingLog) {
        const logEntry = document.createElement('div');
        logEntry.textContent = `[${new Date().toLocaleTimeString()}] ${data.message}`;
        processingLog.appendChild(logEntry);
        processingLog.scrollTop = processingLog.scrollHeight;
    }
}

// Handle step completion
function handleStepComplete(data) {
    const stepNumber = data.step;
    const allSteps = document.querySelectorAll('#processing-steps li');
    
    // Mark current step as complete
    const currentStep = document.getElementById(`step-${stepNumber}`);
    if (currentStep) {
        currentStep.classList.remove('text-blue-700');
        currentStep.classList.add('text-green-700');
        currentStep.querySelector('span:first-child').classList.remove('bg-blue-500');
        currentStep.querySelector('span:first-child').classList.add('bg-green-500');
    }
    
    // Activate next step if available
    if (stepNumber < allSteps.length) {
        const nextStep = document.getElementById(`step-${stepNumber + 1}`);
        if (nextStep) {
            nextStep.classList.remove('text-gray-500');
            nextStep.classList.add('text-blue-700');
            nextStep.querySelector('span:first-child').classList.remove('bg-gray-300');
            nextStep.querySelector('span:first-child').classList.add('bg-blue-500');
        }
    }
}

// Handle processing completion
function handleProcessingComplete(data) {
    // Mark all steps as complete
    document.querySelectorAll('#processing-steps li').forEach((step, index) => {
        step.classList.remove('text-gray-500', 'text-blue-700');
        step.classList.add('text-green-700');
        step.querySelector('span:first-child').classList.remove('bg-gray-300', 'bg-blue-500');
        step.querySelector('span:first-child').classList.add('bg-green-500');
    });
    
    // Update progress to 100%
    const progressBar = document.getElementById('progress-bar');
    const progressPercentage = document.getElementById('progress-percentage');
    progressBar.style.width = '100%';
    progressPercentage.textContent = '100%';
    
    // Show result container with success animation
    const resultContainer = document.getElementById('result-container');
    resultContainer.classList.remove('hidden');
    resultContainer.classList.add('success-pulse');
    
    // Remove the animation class after it completes
    setTimeout(() => {
        resultContainer.classList.remove('success-pulse');
    }, 3000);
    
    // Set video source
    const resultVideo = document.getElementById('result-video');
    resultVideo.src = `/outputs/${data.video_path}`;
    currentVideoPath = data.video_path;
    
    // Update video information
    document.getElementById('video-duration').textContent = formatDuration(data.duration);
    document.getElementById('video-resolution').textContent = data.resolution;
    document.getElementById('video-size').textContent = `${(data.size / (1024 * 1024)).toFixed(2)} MB`;
    document.getElementById('video-date').textContent = new Date().toLocaleDateString();
    
    // Set download link
    const downloadBtn = document.getElementById('download-btn');
    downloadBtn.href = `/outputs/${data.video_path}`;
    downloadBtn.download = data.video_path;
    
    // Update YouTube form if available
    const youtubeTitle = document.getElementById('youtube-title');
    const youtubeDescription = document.getElementById('youtube-description');
    if (youtubeTitle && youtubeDescription) {
        const currentDate = new Date().toLocaleDateString();
        youtubeTitle.value = `My Memories - ${currentDate}`;
        
        // Create a detailed description with timestamps for each media item
        let description = `Slideshow created on ${currentDate} with ${data.stats.total_files} media files.\n\n`;
        
        // Add detailed information about the slideshow
        description += `📊 Slideshow Statistics:\n`;
        description += `• Total Duration: ${formatDuration(data.duration)}\n`;
        description += `• Resolution: ${data.resolution}\n`;
        description += `• Media Files: ${data.stats.total_files} (${data.stats.image_count || 0} images, ${data.stats.video_count || 0} videos)\n\n`;
        
        // Add detailed timestamps section
        if (data.timestamps && data.timestamps.length > 0) {
            description += `⏱️ Detailed Timestamps:\n`;
            data.timestamps.forEach((ts, index) => {
                const minutes = Math.floor(ts.time / 60);
                const seconds = Math.floor(ts.time % 60);
                const timeFormatted = `${minutes}:${seconds.toString().padStart(2, '0')}`;
                const icon = ts.type === 'video' ? '🎬' : '🖼️';
                description += `${icon} ${timeFormatted} - ${ts.name}\n`;
            });
            description += '\n';
        }
        
        // Add footer
        description += `🔄 Created with Memento - Memory Slideshow Creator\n`;
        description += `🖥️ GPU-accelerated video processing for high quality results`;
        
        youtubeDescription.value = description;
    }
    
    // Update timestamps list
    if (data.timestamps) {
        updateTimestampsList(data.timestamps);
    }
    
    // Scroll to result
    resultContainer.scrollIntoView({ behavior: 'smooth' });
    
    // Celebrate with confetti!
    if (typeof window.launchConfetti === 'function') {
        console.log('Launching confetti celebration');
        window.launchConfetti();
    } else {
        console.log('Confetti function not available, loading script');
        // Dynamically load the confetti script if not already loaded
        const script = document.createElement('script');
        script.src = '/static/js/confetti.js';
        script.onload = function() {
            console.log('Confetti script loaded, launching celebration');
            window.launchConfetti();
        };
        document.head.appendChild(script);
    }
    
    // Switch to the result tab if we're using the tabbed interface
    if (typeof showTab === 'function') {
        showTab(3); // Switch to Result tab
    }
}

// Handle processing errors
function handleProcessingError(data) {
    showError(data.error);
    document.getElementById('progress-container').classList.add('hidden');
}

// Update timestamps list
function updateTimestampsList(timestamps) {
    if (!timestamps || !timestampsList) return;
    
    timestampsList.innerHTML = '';
    timestampsList.dataset.timestamps = JSON.stringify(timestamps);
    
    timestamps.forEach(ts => {
        const minutes = Math.floor(ts.time / 60);
        const seconds = Math.floor(ts.time % 60);
        const timeFormatted = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        const li = document.createElement('li');
        li.className = 'py-2 flex items-center';
        
        const icon = ts.type === 'video' ? 'fa-video' : 'fa-image';
        li.innerHTML = `
            <i class="fas ${icon} text-gray-500 mr-3"></i>
            <span class="text-gray-800 font-medium">${timeFormatted}</span>
            <span class="mx-2 text-gray-400">-</span>
            <span class="text-gray-600">${ts.name}</span>
        `;
        
        timestampsList.appendChild(li);
    });
}

// Format duration in seconds to MM:SS
function formatDuration(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs.toString().padStart(2, '0')}`;
}

// Initialize on DOM content loaded
document.addEventListener('DOMContentLoaded', initializeSocketConnection);
