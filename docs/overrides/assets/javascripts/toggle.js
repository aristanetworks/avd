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

  // Helper function to find the first major element currently in the viewport
  const findFirstVisibleElement = () => {
    // This selector targets common content blocks like paragraphs and code blocks.
    const elements = document.querySelectorAll('.md-content__inner p, .md-content__inner pre, .md-content__inner table');
    for (let i = 0; i < elements.length; i++) {
        const rect = elements[i].getBoundingClientRect();
        // Return the first element that is at least partially visible from the top.
        if (rect.top >= 0 && rect.top < window.innerHeight) {
            return elements[i];
        }
    }
    return null;
  };

  const switchToTab = (tabName, preserveScroll) => {
    let anchorElement = null;
    let anchorOffsetTop = 0;

    // Step 1: If preserving scroll, find our anchor element and its offset.
    if (preserveScroll) {
        anchorElement = findFirstVisibleElement();
        if (anchorElement) {
            anchorOffsetTop = anchorElement.getBoundingClientRect().top;
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
      // The timeout ensures this runs after the browser has processed the reflow.
      setTimeout(() => {
        const newRect = anchorElement.getBoundingClientRect();
        const scrollByAmount = newRect.top - anchorOffsetTop;
        window.scrollBy({
          top: scrollByAmount,
          left: 0,
          behavior: "instant"
        });
      }, 0);
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