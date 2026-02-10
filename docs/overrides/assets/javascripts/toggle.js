// docs/overrides/assets/javascripts/toggle.js

// Use the official Material for MkDocs JavaScript API.
document$.subscribe(function() {
  const switchInput = document.getElementById("code-lang-switch");

  if (!switchInput) {
    return;
  }

  const LANG_A = "Table";
  const LANG_B = "YAML";
  const STORAGE_KEY = 'preferred-code-language';

  // Create loading overlay if it doesn't exist
  let loadingOverlay = document.getElementById("toggle-loading-overlay");
  if (!loadingOverlay) {
    loadingOverlay = document.createElement("div");
    loadingOverlay.id = "toggle-loading-overlay";
    loadingOverlay.className = "toggle-loading-overlay";
    loadingOverlay.innerHTML = '<div class="toggle-spinner"></div>';
    document.body.appendChild(loadingOverlay);
  }

  const showLoading = () => {
    loadingOverlay.classList.add("active");
  };

  const hideLoading = () => {
    loadingOverlay.classList.remove("active");
  };

  // Find the best anchor element and calculate offset from it
  const findScrollAnchor = () => {
    const headings = document.querySelectorAll('.md-content__inner h1, .md-content__inner h2, .md-content__inner h3, .md-content__inner h4, .md-content__inner h5, .md-content__inner h6');
    const currentScrollY = window.scrollY;
    const headerOffset = 80; // Account for sticky header

    let anchorElement = null;

    // Find the last heading that is above or at the current scroll position
    for (const heading of headings) {
      const headingTop = heading.getBoundingClientRect().top + window.scrollY;
      if (headingTop <= currentScrollY + headerOffset + 50) {
        anchorElement = heading;
      } else {
        break;
      }
    }

    if (anchorElement) {
      const anchorTop = anchorElement.getBoundingClientRect().top + window.scrollY;
      return {
        element: anchorElement,
        offset: currentScrollY - anchorTop
      };
    }

    return null;
  };

  // Restore scroll position relative to anchor
  const restoreScrollPosition = (anchor) => {
    if (!anchor || !anchor.element) return;

    // Wait for DOM to reflow after tab switch
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        const newAnchorTop = anchor.element.getBoundingClientRect().top + window.scrollY;
        const newScrollY = newAnchorTop + anchor.offset;

        window.scroll({
          top: Math.max(0, newScrollY),
          left: 0,
          behavior: "instant"
        });
      });
    });
  };

  const switchToTab = (tabName, preserveScroll, scrollAnchor) => {
    // Step 1: Switch all the tabs by finding and clicking the first matching label.
    // Material for MkDocs with content.tabs.link will sync all other tabs automatically.
    const tabLabels = document.querySelectorAll(".md-typeset .tabbed-labels > label");
    if (tabLabels.length === 0) {
      return;
    }

    // Find and click the first matching tab label - Material will sync the rest
    for (const label of tabLabels) {
      if (label.textContent.trim().toLowerCase() === tabName.toLowerCase()) {
        label.click();
        break; // Only need to click one - content.tabs.link syncs the rest
      }
    }

    // Step 2: Restore scroll position if we have an anchor
    if (preserveScroll && scrollAnchor) {
      restoreScrollPosition(scrollAnchor);
    }
  };

  // --- INITIALIZATION AND EVENT HANDLING ---
  const savedLang = localStorage.getItem(STORAGE_KEY);
  const initialLang = (savedLang === LANG_B) ? LANG_B : LANG_A;
  switchInput.checked = (initialLang === LANG_B);

  // Delay initial tab switch to ensure DOM is fully ready (no scroll preservation needed)
  requestAnimationFrame(() => {
    switchToTab(initialLang, false, null);
  });

  if (!switchInput.hasAttribute('data-listener-attached')) {
    switchInput.addEventListener("change", (event) => {
      const targetLang = event.target.checked ? LANG_B : LANG_A;

      // Capture scroll anchor BEFORE showing spinner or switching tabs
      const scrollAnchor = findScrollAnchor();

      // Show loading spinner
      showLoading();

      // Use setTimeout to allow the spinner to render before switching tabs
      setTimeout(() => {
        switchToTab(targetLang, true, scrollAnchor);
        localStorage.setItem(STORAGE_KEY, targetLang);

        // Hide loading spinner after scroll restoration completes
        setTimeout(() => {
          hideLoading();
        }, 100);
      }, 50);
    });
    switchInput.setAttribute('data-listener-attached', 'true');
  }
});
