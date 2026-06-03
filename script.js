function initPublicationTabs() {
  const section = document.getElementById("publications");
  if (!section) return;

  const buttons = section.querySelectorAll("[data-pub-tab]");
  const panels = section.querySelectorAll("[data-pub-panel]");
  if (!buttons.length || !panels.length) return;

  const openTab = (tabName) => {
    buttons.forEach((btn) => {
      const selected = btn.dataset.pubTab === tabName;
      btn.classList.toggle("active", selected);
      btn.setAttribute("aria-selected", selected ? "true" : "false");
    });
    panels.forEach((panel) => {
      panel.classList.toggle("tab-open", panel.dataset.pubPanel === tabName);
    });
  };

  buttons.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      openTab(btn.dataset.pubTab);
    });
  });

  openTab(buttons[0].dataset.pubTab);
}

function initAchievementTabs() {
  const section = document.getElementById("achievement");
  if (!section) return;

  const buttons = section.querySelectorAll("[data-ach-tab]");
  const panels = section.querySelectorAll("[data-ach-panel]");
  if (!buttons.length || !panels.length) return;

  const openTab = (tabName) => {
    buttons.forEach((btn) => {
      const selected = btn.dataset.achTab === tabName;
      btn.classList.toggle("active", selected);
      btn.setAttribute("aria-selected", selected ? "true" : "false");
    });
    panels.forEach((panel) => {
      panel.classList.toggle("tab-open", panel.dataset.achPanel === tabName);
    });
  };

  buttons.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      openTab(btn.dataset.achTab);
    });
  });

  openTab(buttons[0].dataset.achTab);
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

function boot() {
  initPublicationTabs();
  initAchievementTabs();
  initScrollNav();
  initSmoothLinks();
  initTldrToggles();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", boot);
} else {
  boot();
}
