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

  const switchToTab = (tabName) => {
    // This selector specifically targets the content tab links.
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
  };

  const savedLang = localStorage.getItem(STORAGE_KEY);
  const initialLang = (savedLang === LANG_B) ? LANG_B : LANG_A;

  switchInput.checked = (initialLang === LANG_B);
  switchToTab(initialLang);

  if (!switchInput.hasAttribute('data-listener-attached')) {
    switchInput.addEventListener("change", (event) => {
      const targetLang = event.target.checked ? LANG_B : LANG_A;
      switchToTab(targetLang);
      localStorage.setItem(STORAGE_KEY, targetLang);
    });
    switchInput.setAttribute('data-listener-attached', 'true');
  }
});