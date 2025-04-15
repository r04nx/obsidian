// YouTube upload functionality
function initializeYouTubeUpload() {
    const youtubeForm = document.getElementById('youtube-form');
    const youtubeTitle = document.getElementById('youtube-title');
    const youtubeDescription = document.getElementById('youtube-description');
    const youtubeUploadBtn = document.getElementById('youtube-upload-btn');
    const uploadStatus = document.getElementById('youtube-upload-status');
    const timestampsList = document.getElementById('timestamps-list');
    
    // Toggle YouTube options
    const youtubeToggleBtn = document.getElementById('youtube-toggle-btn');
    const youtubeOptions = document.getElementById('youtube-options');
    const youtubeCancelBtn = document.getElementById('youtube-cancel-btn');
    const youtubeSuccessDiv = document.getElementById('youtube-success');
    const youtubeDoneBtn = document.getElementById('youtube-done-btn');
    
    if (youtubeToggleBtn) {
        youtubeToggleBtn.addEventListener('click', function() {
            youtubeOptions.classList.toggle('hidden');
            console.log('YouTube options toggled');
        });
    }
    
    if (youtubeCancelBtn) {
        youtubeCancelBtn.addEventListener('click', function() {
            youtubeOptions.classList.add('hidden');
            console.log('YouTube options canceled');
        });
    }
    
    if (youtubeDoneBtn) {
        youtubeDoneBtn.addEventListener('click', function() {
            youtubeSuccessDiv.classList.add('hidden');
        });
    }
    
    // Handle form submission
    if (youtubeForm) {
        console.log('YouTube form found, adding event listener');
        
        youtubeForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log('YouTube form submitted');
            
            if (!currentVideoPath) {
                showError('No video available to upload');
                return;
            }
            
            // Get form values
            const title = youtubeTitle.value || 'My Memories Slideshow';
            const description = youtubeDescription.value || 'Created with Memento Slideshow Creator';
            const privacy = document.querySelector('input[name="privacy"]:checked')?.value || 'private';
            
            console.log('Upload details:', { title, privacy, videoPath: currentVideoPath });
            
            // Update UI
            youtubeUploadBtn.disabled = true;
            youtubeUploadBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Uploading...';
            uploadStatus.textContent = 'Connecting to YouTube...';
            uploadStatus.classList.remove('hidden');
            
            // Create request data
            const requestData = {
                video_path: currentVideoPath,
                title: title,
                description: description,
                privacy: privacy,
                timestamps: timestampsList && timestampsList.dataset.timestamps ? JSON.parse(timestampsList.dataset.timestamps) : []
            };
            
            console.log('Sending request with data:', requestData);
            
            // Send the request
            fetch('/upload-to-youtube', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            })
            .then(response => {
                console.log('Response received:', response.status);
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log('Upload success data:', data);
                if (data.success) {
                    uploadStatus.innerHTML = `<i class="fas fa-check-circle text-green-500 mr-2"></i>Upload successful! <a href="${data.youtube_url}" target="_blank" class="text-blue-500 hover:underline">View on YouTube</a>`;
                    
                    // Show success screen if available
                    if (youtubeSuccessDiv) {
                        const youtubeLink = document.getElementById('youtube-link');
                        if (youtubeLink) {
                            youtubeLink.href = data.youtube_url;
                            youtubeLink.textContent = data.youtube_url;
                        }
                        youtubeOptions.classList.add('hidden');
                        youtubeSuccessDiv.classList.remove('hidden');
                    }
                    
                    createConfetti();
                } else {
                    throw new Error(data.error || 'Upload failed');
                }
            })
            .catch(error => {
                console.error('Upload error:', error);
                uploadStatus.innerHTML = `<i class="fas fa-exclamation-circle text-red-500 mr-2"></i>${error.message}`;
            })
            .finally(() => {
                youtubeUploadBtn.disabled = false;
                youtubeUploadBtn.innerHTML = '<i class="fab fa-youtube mr-2"></i>Upload to YouTube';
            });
        });
    } else {
        console.error('YouTube form not found!');
    }
}

// Confetti animation
function createConfetti() {
    const confettiCount = 200;
    const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff'];
    
    // Check if canvas is supported
    if (window.innerWidth > 768) {
        const confettiContainer = document.createElement('div');
        confettiContainer.className = 'fixed inset-0 pointer-events-none z-50';
        document.body.appendChild(confettiContainer);
        
        for (let i = 0; i < confettiCount; i++) {
            const confetti = document.createElement('div');
            confetti.className = 'absolute w-2 h-3 rounded-sm pointer-events-none';
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.left = `${Math.random() * 100}%`;
            confetti.style.top = '-10px';
            confetti.style.transform = `rotate(${Math.random() * 360}deg)`;
            confetti.style.opacity = Math.random() + 0.5;
            confetti.style.animation = `confetti-fall ${Math.random() * 3 + 2}s linear forwards`;
            confettiContainer.appendChild(confetti);
        }
        
        setTimeout(() => {
            document.body.removeChild(confettiContainer);
        }, 5000);
    }
}

// Initialize on DOM content loaded
document.addEventListener('DOMContentLoaded', initializeYouTubeUpload);
