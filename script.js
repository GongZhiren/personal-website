function initScopedTabs(rootSelector, buttonSelector, panelSelector) {
  const root = document.querySelector(rootSelector);
  if (!root) return;

  const buttons = root.querySelectorAll(buttonSelector);
  const panels = root.querySelectorAll(panelSelector);
  if (!buttons.length || !panels.length) return;

  const activate = (targetId) => {
    buttons.forEach((btn) => {
      btn.classList.toggle("active", btn.dataset.target === targetId);
    });
    panels.forEach((panel) => {
      panel.classList.toggle("is-active", panel.id === targetId);
    });
  };

  buttons.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      const targetId = btn.dataset.target;
      if (!targetId) return;
      activate(targetId);
    });
  });

  const defaultBtn = root.querySelector(`${buttonSelector}.active`) || buttons[0];
  if (defaultBtn?.dataset.target) {
    activate(defaultBtn.dataset.target);
  }
}

function initScrollNav() {
  const links = [...document.querySelectorAll(".top-nav a")];
  const sections = links
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if (!sections.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = `#${entry.target.id}`;
        links.forEach((link) => {
          const active = link.getAttribute("href") === id;
          link.classList.toggle("active", active);
        });
      });
    },
    { threshold: 0.35 }
  );

  sections.forEach((section) => observer.observe(section));
}

function initSmoothLinks() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (event) => {
      const href = anchor.getAttribute("href");
      if (!href || href === "#") return;
      const target = document.querySelector(href);
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
}

function initTldrToggles() {
  const toggles = document.querySelectorAll(".tldr-toggle");
  if (!toggles.length) return;

  toggles.forEach((toggle) => {
    toggle.addEventListener("click", () => {
      const targetId = toggle.dataset.target;
      if (!targetId) return;
      const panel = document.getElementById(targetId);
      if (!panel) return;
      panel.classList.toggle("open");
    });
  });
}

initScopedTabs("#publications", ".pub-tab-btn", ".pub-panel");
initScopedTabs("#achievement", ".achievement-tab-btn", ".achievement-panel");
initScrollNav();
initSmoothLinks();
initTldrToggles();
