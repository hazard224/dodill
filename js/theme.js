// Light/dark switch. Follows the system setting until the visitor picks one.
(function () {
  var root = document.documentElement;
  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function current() { return root.getAttribute('data-theme') || (mq && mq.matches ? 'dark' : 'light'); }
  function label(btn) {
    var next = current() === 'dark' ? 'light' : 'dark';
    btn.setAttribute('aria-label', 'Switch to ' + next + ' mode');
    btn.setAttribute('aria-pressed', current() === 'dark' ? 'true' : 'false');
    btn.querySelector('.theme-word').textContent = next === 'dark' ? 'Dark' : 'Light';
  }
  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;
    label(btn);
    btn.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
      label(btn);
    });
    if (mq && mq.addEventListener) mq.addEventListener('change', function () { label(btn); });
  });
})();
