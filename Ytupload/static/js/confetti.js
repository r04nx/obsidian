/**
 * Simple Confetti Animation
 * A lightweight confetti animation that works in all browsers
 */

// Main confetti function
function launchConfetti() {
  console.log('Launching confetti animation');
  
  // Create canvas element
  const canvas = document.createElement('canvas');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '9999';
  document.body.appendChild(canvas);
  
  // Get canvas context
  const ctx = canvas.getContext('2d');
  
  // Confetti particles
  const particles = [];
  const particleCount = 200;
  const colors = [
    '#f44336', '#e91e63', '#9c27b0', '#673ab7', 
    '#3f51b5', '#2196f3', '#03a9f4', '#00bcd4', 
    '#009688', '#4caf50', '#8bc34a', '#cddc39', 
    '#ffeb3b', '#ffc107', '#ff9800', '#ff5722'
  ];
  
  // Create particles
  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height - canvas.height,
      radius: Math.random() * 5 + 5,
      color: colors[Math.floor(Math.random() * colors.length)],
      speed: Math.random() * 3 + 2,
      rotation: Math.random() * 360,
      rotationSpeed: Math.random() * 5 - 2.5,
      shape: Math.random() > 0.5 ? 'circle' : (Math.random() > 0.5 ? 'square' : 'triangle')
    });
  }
  
  // Play celebration sound
  try {
    const audio = new Audio('/static/sounds/celebration.mp3');
    audio.volume = 0.5;
    audio.play().catch(e => console.log('Could not play celebration sound', e));
  } catch (e) {
    console.log('Celebration sound not available');
  }
  
  // Animation function
  let animationFrame;
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    let stillFalling = false;
    
    // Draw each particle
    particles.forEach(p => {
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate((p.rotation * Math.PI) / 180);
      
      // Draw different shapes
      if (p.shape === 'circle') {
        ctx.beginPath();
        ctx.arc(0, 0, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
      } else if (p.shape === 'square') {
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.radius, -p.radius, p.radius * 2, p.radius * 2);
      } else {
        // Triangle
        ctx.beginPath();
        ctx.moveTo(0, -p.radius);
        ctx.lineTo(-p.radius, p.radius);
        ctx.lineTo(p.radius, p.radius);
        ctx.closePath();
        ctx.fillStyle = p.color;
        ctx.fill();
      }
      
      ctx.restore();
      
      // Update position
      p.y += p.speed;
      p.rotation += p.rotationSpeed;
      
      // Check if still falling
      if (p.y < canvas.height + p.radius) {
        stillFalling = true;
      }
    });
    
    // Continue animation if particles are still falling
    if (stillFalling) {
      animationFrame = requestAnimationFrame(animate);
    } else {
      // Clean up when done
      cancelAnimationFrame(animationFrame);
      document.body.removeChild(canvas);
      console.log('Confetti animation complete');
    }
  }
  
  // Start animation
  animate();
  
  // Clean up after 6 seconds (failsafe)
  setTimeout(() => {
    if (document.body.contains(canvas)) {
      cancelAnimationFrame(animationFrame);
      document.body.removeChild(canvas);
      console.log('Confetti animation cleaned up (timeout)');
    }
  }, 6000);
}

// Make available globally
window.launchConfetti = launchConfetti;
