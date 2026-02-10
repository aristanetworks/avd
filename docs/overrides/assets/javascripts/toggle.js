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

  const switchToTab = (tabName, preserveScroll) => {
    let anchorElement = null;
    let scrollOffset = 0;

    // Step 1: If preserving scroll, find a stable anchor (the nearest heading
    // above the viewport) and calculate the user's offset from it.
    if (preserveScroll) {
      const headings = document.querySelectorAll('.md-content__inner h1, .md-content__inner h2, .md-content__inner h3, .md-content__inner h4');
      const currentScrollY = window.scrollY;

      // Find the last heading that is located above the current top of the viewport.
      for (const heading of headings) {
        if (heading.offsetTop < currentScrollY) {
          anchorElement = heading;
        } else {
          // We've gone past the current view, so the previous heading was our anchor.
          break;
        }
      }

      // If we found a stable anchor, calculate how far down from it the user has scrolled.
      if (anchorElement) {
        scrollOffset = currentScrollY - anchorElement.offsetTop;
      }
    }

    // Step 2: Switch all the tabs by finding and clicking the first matching label.
    // Material for MkDocs with content.tabs.link will sync all other tabs automatically.
    const tabLabels = document.querySelectorAll(".md-typeset .tabbed-labels > label");
    if (tabLabels.length === 0) {
      console.log("No tab labels found");
      return;
    }

    // Find and click the first matching tab label - Material will sync the rest
    let clicked = false;
    for (const label of tabLabels) {
      if (label.textContent.trim().toLowerCase() === tabName.toLowerCase()) {
        console.log("Clicking tab:", label.textContent.trim());
        label.click();
        clicked = true;
        break; // Only need to click one - content.tabs.link syncs the rest
      }
    }

    if (!clicked) {
      console.log("No matching tab found for:", tabName);
    }

    // Step 3: If we have an anchor, restore the scroll position relative to it.
    if (preserveScroll && anchorElement) {
      // The timeout gives the browser a moment to reflow the content.
      requestAnimationFrame(() => {
        // Calculate the new required scroll position based on the anchor's
        // (potentially new) position and the original offset.
        const newScrollY = anchorElement.offsetTop + scrollOffset;

        window.scroll({
          top: newScrollY,
          left: 0,
          behavior: "instant"
        });
      });
    }
  };

  // --- INITIALIZATION AND EVENT HANDLING ---
  const savedLang = localStorage.getItem(STORAGE_KEY);
  const initialLang = (savedLang === LANG_B) ? LANG_B : LANG_A;
  switchInput.checked = (initialLang === LANG_B);

  // Delay initial tab switch to ensure DOM is fully ready
  requestAnimationFrame(() => {
    switchToTab(initialLang, false);
  });

  if (!switchInput.hasAttribute('data-listener-attached')) {
    switchInput.addEventListener("change", (event) => {
      const targetLang = event.target.checked ? LANG_B : LANG_A;
      console.log("Toggle changed to:", targetLang);
      switchToTab(targetLang, true);
      localStorage.setItem(STORAGE_KEY, targetLang);
    });
    switchInput.setAttribute('data-listener-attached', 'true');
  }
});
