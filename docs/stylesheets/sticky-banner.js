// Hide custom banner when header autohides
document.addEventListener("DOMContentLoaded", function() {
  const banner = document.querySelector('.custom-banner');
  const header = document.querySelector('.md-header');

  if (!banner) {
    console.log('Custom banner not found');
    return;
  }

  if (!header) {
    console.log('Header not found');
    return;
  }

  console.log('Banner and header found, setting up observer');

  // Function to check if header is hidden
  function checkHeaderVisibility() {
    // MkDocs Material adds 'hidden' class or changes transform when header hides
    const headerStyle = window.getComputedStyle(header);
    const transform = headerStyle.transform;
    const isHidden = transform && transform !== 'none' && transform.includes('matrix');

    // Check if header has moved up (negative translateY)
    if (transform && transform !== 'none') {
      const matrix = transform.match(/matrix.*\((.+)\)/);
      if (matrix) {
        const values = matrix[1].split(', ');
        const translateY = parseFloat(values[5] || values[13]); // 2D or 3D matrix

        if (translateY < -10) {
          // Header is hidden (moved up)
          banner.classList.add('header-hidden');
          console.log('Header hidden - hiding banner');
        } else {
          // Header is visible
          banner.classList.remove('header-hidden');
          console.log('Header visible - showing banner');
        }
      }
    } else {
      // No transform, header is visible
      banner.classList.remove('header-hidden');
    }
  }

  // Watch for transform changes on the header
  const observer = new MutationObserver(function(mutations) {
    checkHeaderVisibility();
  });

  observer.observe(header, {
    attributes: true,
    attributeFilter: ['style', 'class', 'data-md-state']
  });

  // Also check on scroll
  let ticking = false;
  window.addEventListener('scroll', function() {
    if (!ticking) {
      window.requestAnimationFrame(function() {
        checkHeaderVisibility();
        ticking = false;
      });
      ticking = true;
    }
  });

  // Initial check
  checkHeaderVisibility();
});
