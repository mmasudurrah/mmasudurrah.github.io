// Progressive enhancement: native links and all content work without JavaScript.
(() => {
  const header = document.querySelector('.site-header');
  const button = header.querySelector('.menu-toggle');
  const nav = header.querySelector('nav');
  const mobile = matchMedia('(max-width: 900px)');
  const jumps = [...document.querySelectorAll('.section-jump')];
  header.dataset.enhanced = '';
  button.hidden = false;

  function sizeHeader() {
    // An expanded menu overlays content; anchor offsets use the closed header.
    if (!header.classList.contains('menu-open')) {
      document.documentElement.style.setProperty('--header-height', `${header.offsetHeight}px`);
    }
  }
  function closeMenu() {
    header.classList.remove('menu-open');
    button.setAttribute('aria-expanded', 'false');
    sizeHeader();
  }
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    header.classList.toggle('menu-open', open);
    button.setAttribute('aria-expanded', String(open));
  });
  header.addEventListener('keydown', event => {
    if (event.key === 'Escape' && header.classList.contains('menu-open')) {
      closeMenu();
      button.focus();
    }
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  function setJumpLayout() {
    closeMenu();
    jumps.forEach(jump => { jump.open = !mobile.matches; });
  }
  for (const jump of jumps) {
    jump.addEventListener('click', event => {
      const link = event.target.closest('a');
      if (!link || !mobile.matches) return;
      const target = document.getElementById(new URL(link.href).hash.slice(1));
      jump.open = false;
      // Move keyboard focus with the selected section; keep native URL/history.
      if (target) {
        target.setAttribute('tabindex', '-1');
        target.focus({preventScroll:true});
      }
    });
    // Desktop indexes remain expanded; keyboard activation behaves consistently.
    jump.querySelector('summary').addEventListener('click', event => {
      if (!mobile.matches) event.preventDefault();
    });
  }
  mobile.addEventListener('change', setJumpLayout);
  window.addEventListener('pageshow', closeMenu);
  new ResizeObserver(sizeHeader).observe(header);
  setJumpLayout();
})();
