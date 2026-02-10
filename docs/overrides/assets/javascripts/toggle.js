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

  // Find the tab container currently visible in the viewport
  const findScrollAnchor = () => {
    const headerOffset = 80; // Account for sticky header
    const viewportTop = window.scrollY + headerOffset;
    const viewportCenter = viewportTop + (window.innerHeight / 3); // Upper third of visible area

    // First, try to find a tabbed container that's currently in view
    const tabbedContainers = document.querySelectorAll('.md-typeset .tabbed-set');
    let bestContainer = null;
    let bestDistance = Infinity;

    for (const container of tabbedContainers) {
      const rect = container.getBoundingClientRect();
      const containerTop = rect.top + window.scrollY;
      const containerBottom = containerTop + rect.height;

      // Check if this container is visible in the viewport
      if (containerBottom > viewportTop && containerTop < viewportTop + window.innerHeight) {
        // Find the container closest to the top of the viewport
        const distance = Math.abs(containerTop - viewportTop);
        if (distance < bestDistance) {
          bestDistance = distance;
          bestContainer = container;
        }
      }
    }

    if (bestContainer) {
      const containerTop = bestContainer.getBoundingClientRect().top + window.scrollY;
      return {
        element: bestContainer,
        offset: window.scrollY - containerTop,
        type: 'tabbed-set'
      };
    }

    // Fallback: find the nearest heading
    const headings = document.querySelectorAll('.md-content__inner h1, .md-content__inner h2, .md-content__inner h3, .md-content__inner h4, .md-content__inner h5, .md-content__inner h6');
    let anchorElement = null;

    for (const heading of headings) {
      const headingTop = heading.getBoundingClientRect().top + window.scrollY;
      if (headingTop <= viewportCenter) {
        anchorElement = heading;
      } else {
        break;
      }
    }

    if (anchorElement) {
      const anchorTop = anchorElement.getBoundingClientRect().top + window.scrollY;
      return {
        element: anchorElement,
        offset: window.scrollY - anchorTop,
        type: 'heading'
      };
    }

    return null;
  };

  // Restore scroll position relative to anchor
  const restoreScrollPosition = (anchor) => {
    if (!anchor || !anchor.element) return;

    // Wait for DOM to reflow after tab switch - use multiple frames for large content changes
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        setTimeout(() => {
          const newAnchorTop = anchor.element.getBoundingClientRect().top + window.scrollY;

          // For tabbed containers, scroll to show the container at the same relative position
          // For headings, restore the exact offset
          let newScrollY;
          if (anchor.type === 'tabbed-set') {
            // Keep the container at roughly the same position relative to viewport top
            newScrollY = newAnchorTop + Math.min(anchor.offset, 0);
          } else {
            newScrollY = newAnchorTop + anchor.offset;
          }

          window.scroll({
            top: Math.max(0, newScrollY),
            left: 0,
            behavior: "instant"
          });
        }, 50); // Additional delay for large DOM changes
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

  // Flag to prevent circular updates when we programmatically click tabs
  let isToggleSwitching = false;

  // Sync toggle button state based on which tab is active
  const syncToggleState = (tabName) => {
    if (isToggleSwitching) return; // Don't sync if we triggered the change

    const isYaml = tabName.toLowerCase() === LANG_B.toLowerCase();
    if (switchInput.checked !== isYaml) {
      switchInput.checked = isYaml;
      localStorage.setItem(STORAGE_KEY, isYaml ? LANG_B : LANG_A);
    }
  };

  // Listen for clicks on tab labels to sync toggle state
  const tabLabels = document.querySelectorAll(".md-typeset .tabbed-labels > label");
  tabLabels.forEach(label => {
    label.addEventListener("click", () => {
      const tabName = label.textContent.trim();
      // Only sync if it's a Table or YAML tab
      if (tabName.toLowerCase() === LANG_A.toLowerCase() ||
          tabName.toLowerCase() === LANG_B.toLowerCase()) {
        syncToggleState(tabName);
      }
    });
  });

  if (!switchInput.hasAttribute('data-listener-attached')) {
    switchInput.addEventListener("change", (event) => {
      const targetLang = event.target.checked ? LANG_B : LANG_A;

      // Capture scroll anchor BEFORE showing spinner or switching tabs
      const scrollAnchor = findScrollAnchor();

      // Show loading spinner
      showLoading();

      // Set flag to prevent circular sync
      isToggleSwitching = true;

      // Use setTimeout to allow the spinner to render before switching tabs
      setTimeout(() => {
        switchToTab(targetLang, true, scrollAnchor);
        localStorage.setItem(STORAGE_KEY, targetLang);

        // Reset flag after tabs have switched
        setTimeout(() => {
          isToggleSwitching = false;
          hideLoading();
        }, 100);
      }, 50);
    });
    switchInput.setAttribute('data-listener-attached', 'true');
  }
});
