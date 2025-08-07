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
        for (let i = 0; i < headings.length; i++) {
            if (headings[i].offsetTop < currentScrollY) {
                anchorElement = headings[i];
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

    // Step 2: Switch all the tabs by checking the underlying radio buttons.
    const tabLinks = document.querySelectorAll("a[href^='#__tabbed_']");
    if (tabLinks.length === 0) {
        return;
    }
    tabLinks.forEach(link => {
      if (link.textContent.trim().toLowerCase() === tabName.toLowerCase()) {
        const controlId = link.getAttribute("href").substring(1);
        const radioInput = document.getElementById(controlId);
        if (radioInput) {
          radioInput.checked = true;
        }
      }
    });

    // Step 3: If we have an anchor, restore the scroll position relative to it.
    if (preserveScroll && anchorElement) {
      // The timeout gives the browser a moment to reflow the content.
      setTimeout(() => {
        // Calculate the new required scroll position based on the anchor's
        // (potentially new) position and the original offset.
        const newScrollY = anchorElement.offsetTop + scrollOffset;

        window.scroll({
          top: newScrollY,
          left: 0,
          behavior: "instant"
        });
      }, 10); // Using a slightly longer delay for more stability.
    }
  };

  // --- INITIALIZATION AND EVENT HANDLING (No changes needed) ---
  const savedLang = localStorage.getItem(STORAGE_KEY);
  const initialLang = (savedLang === LANG_B) ? LANG_B : LANG_A;
  switchInput.checked = (initialLang === LANG_B);
  switchToTab(initialLang, false);

  if (!switchInput.hasAttribute('data-listener-attached')) {
    switchInput.addEventListener("change", (event) => {
      const targetLang = event.target.checked ? LANG_B : LANG_A;
      switchToTab(targetLang, true);
      localStorage.setItem(STORAGE_KEY, targetLang);
    });
    switchInput.setAttribute('data-listener-attached', 'true');
  }
});
