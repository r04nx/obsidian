// File Upload Handling
const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('file-input');
const uploadForm = document.getElementById('upload-form');
const uploadBtn = document.getElementById('upload-btn');
const fileListContainer = document.getElementById('file-list-container');
const fileList = document.getElementById('file-list');
const fileCount = document.getElementById('file-count');
const totalSize = document.getElementById('total-size');
const clearFilesBtn = document.getElementById('clear-files-btn');
const collapseFilesBtn = document.getElementById('collapse-files-btn');
const fileListContent = document.getElementById('file-list-content');
const durationSlider = document.getElementById('duration-slider');
const durationValue = document.getElementById('duration-value');
const backgroundAudio = document.getElementById('background-audio');
const audioUploadBtn = document.getElementById('audio-upload-btn');
const audioFileName = document.getElementById('audio-file-name');

// Store uploaded files
let uploadedFiles = [];
let backgroundAudioFile = null;

// Initialize upload functionality
function initializeUpload() {
    // Drag and drop functionality
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight() {
        dropzone.classList.add('border-blue-500', 'bg-blue-50');
    }
    
    function unhighlight() {
        dropzone.classList.remove('border-blue-500', 'bg-blue-50');
    }
    
    // Handle file drop
    dropzone.addEventListener('drop', handleDrop, false);
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    }
    
    // Handle file input change
    dropzone.addEventListener('click', () => {
        fileInput.click();
    });
    
    fileInput.addEventListener('change', () => {
        handleFiles(fileInput.files);
    });
    
    // Handle background audio
    audioUploadBtn.addEventListener('click', () => {
        backgroundAudio.click();
    });
    
    backgroundAudio.addEventListener('change', () => {
        if (backgroundAudio.files.length > 0) {
            backgroundAudioFile = backgroundAudio.files[0];
            audioFileName.textContent = backgroundAudioFile.name;
        } else {
            backgroundAudioFile = null;
            audioFileName.textContent = 'No file selected';
        }
        updateUploadButton();
    });
    
    // Handle file list collapse
    collapseFilesBtn.addEventListener('click', () => {
        fileListContent.classList.toggle('hidden');
        const icon = collapseFilesBtn.querySelector('i');
        if (fileListContent.classList.contains('hidden')) {
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
        } else {
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
        }
    });
    
    // Handle clear files
    clearFilesBtn.addEventListener('click', () => {
        uploadedFiles = [];
        updateFileList();
        fileListContainer.classList.add('hidden');
        updateUploadButton();
    });
    
    // Handle duration slider
    durationSlider.addEventListener('input', updateDurationValue);
    
    // Handle form submission
    uploadForm.addEventListener('submit', handleUpload);
}

// Update duration value display
function updateDurationValue() {
    durationValue.textContent = durationSlider.value;
}

// Process uploaded files
function handleFiles(files) {
    const validFiles = Array.from(files).filter(file => {
        const fileType = file.type.split('/')[0];
        return fileType === 'image' || fileType === 'video';
    });
    
    if (validFiles.length === 0) {
        showError('Please upload valid image or video files');
        return;
    }
    
    validFiles.forEach(file => {
        // Check if file is already in the list
        if (!uploadedFiles.some(f => f.name === file.name && f.size === file.size)) {
            uploadedFiles.push(file);
        }
    });
    
    updateFileList();
    updateUploadButton();
}

// Update the file list UI
function updateFileList() {
    fileList.innerHTML = '';
    fileCount.textContent = uploadedFiles.length;
    
    const totalBytes = uploadedFiles.reduce((acc, file) => acc + file.size, 0);
    const totalMB = (totalBytes / (1024 * 1024)).toFixed(2);
    totalSize.textContent = `${totalMB} MB`;
    
    uploadedFiles.forEach((file, index) => {
        const li = document.createElement('li');
        li.className = 'py-3 flex justify-between items-center';
        
        const fileType = file.type.split('/')[0];
        const icon = fileType === 'image' ? 'fa-image' : 'fa-video';
        const fileSize = (file.size / (1024 * 1024)).toFixed(2);
        
        li.innerHTML = `
            <div class="flex items-center">
                <i class="fas ${icon} text-gray-500 mr-3"></i>
                <div>
                    <p class="text-gray-800 font-medium">${file.name}</p>
                    <p class="text-gray-500 text-sm">${fileSize} MB</p>
                </div>
            </div>
            <button class="text-red-500 hover:text-red-700 transition remove-file" data-index="${index}">
                <i class="fas fa-times"></i>
            </button>
        `;
        
        fileList.appendChild(li);
    });
    
    // Add event listeners to remove buttons
    document.querySelectorAll('.remove-file').forEach(button => {
        button.addEventListener('click', () => {
            const index = parseInt(button.dataset.index);
            uploadedFiles.splice(index, 1);
            updateFileList();
            updateUploadButton();
            
            if (uploadedFiles.length === 0) {
                fileListContainer.classList.add('hidden');
            }
        });
    });
    
    if (uploadedFiles.length > 0) {
        fileListContainer.classList.remove('hidden');
    }
}

// Update upload button state
function updateUploadButton() {
    if (uploadedFiles.length > 0) {
        uploadBtn.disabled = false;
        uploadBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    } else {
        uploadBtn.disabled = true;
        uploadBtn.classList.add('opacity-50', 'cursor-not-allowed');
    }
}

// Handle form submission
function handleUpload(e) {
    e.preventDefault();
    
    if (uploadedFiles.length === 0) {
        showError('Please upload at least one file');
        return;
    }
    
    // Create FormData
    const formData = new FormData();
    uploadedFiles.forEach(file => {
        formData.append('files', file);
    });
    
    formData.append('duration', durationSlider.value);
    
    if (backgroundAudioFile) {
        formData.append('background_audio', backgroundAudioFile);
    }
    
    // Show progress container
    document.getElementById('progress-container').classList.remove('hidden');
    
    // Reset progress UI
    document.getElementById('progress-bar').style.width = '0%';
    document.getElementById('progress-percentage').textContent = '0%';
    document.getElementById('current-operation').textContent = 'Uploading files...';
    
    // Reset steps
    document.querySelectorAll('#processing-steps li').forEach(step => {
        step.classList.remove('text-blue-700', 'text-green-700');
        step.classList.add('text-gray-500');
        step.querySelector('span:first-child').classList.remove('bg-blue-500', 'bg-green-500');
        step.querySelector('span:first-child').classList.add('bg-gray-300');
    });
    
    // Activate first step
    const step1 = document.getElementById('step-1');
    step1.classList.remove('text-gray-500');
    step1.classList.add('text-blue-700');
    step1.querySelector('span:first-child').classList.remove('bg-gray-300');
    step1.querySelector('span:first-child').classList.add('bg-blue-500');
    
    // Upload files
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.error || 'Upload failed');
            });
        }
        return response.json();
    })
    .then(data => {
        console.log('Upload successful:', data);
        // Processing will continue via Socket.IO
    })
    .catch(error => {
        console.error('Upload error:', error);
        showError(error.message);
        document.getElementById('progress-container').classList.add('hidden');
    });
}

// Show error message
function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'fixed top-4 right-4 bg-red-500 text-white px-4 py-3 rounded shadow-lg z-50 error-message';
    errorDiv.innerHTML = `
        <div class="flex items-center">
            <i class="fas fa-exclamation-circle mr-2"></i>
            <span>${message}</span>
        </div>
    `;
    
    document.body.appendChild(errorDiv);
    
    setTimeout(() => {
        errorDiv.classList.add('opacity-0');
        setTimeout(() => {
            document.body.removeChild(errorDiv);
        }, 300);
    }, 3000);
}

// Initialize on DOM content loaded
document.addEventListener('DOMContentLoaded', initializeUpload);
