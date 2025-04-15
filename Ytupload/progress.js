function handleProcessingComplete() {
    // ... existing code ...

    // Add celebration effect
    function celebrateSuccess() {
        const count = 200;
        const defaults = { origin: { y: 0.7 } };
        
        function fire(particleRatio, opts) {
            confetti(Object.assign({}, defaults, opts, {
                particleCount: Math.floor(count * particleRatio)
            }));
        }
        
        // Launch multiple confetti bursts
        fire(0.25, { spread: 26, startVelocity: 55 });
        fire(0.2, { spread: 60 });
        fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
        fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
        fire(0.1, { spread: 120, startVelocity: 45 });
        
        // Optional: Play a celebration sound
        try {
            const audio = new Audio('/static/sounds/celebration.mp3');
            audio.volume = 0.5;
            audio.play().catch(e => console.log('Could not play celebration sound', e));
        } catch (e) {
            console.log('Celebration sound not available');
        }
    }

    // Check if confetti library is loaded
    if (typeof confetti === 'function') {
        celebrateSuccess();
    } else {
        // Load confetti library dynamically if not present
        const script = document.createElement('script');
        script.src = '/static/js/canvas-confetti.min.js';
        script.onload = celebrateSuccess;
        document.head.appendChild(script);
    }
} 