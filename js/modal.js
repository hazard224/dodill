// Case study windows on the portfolio page: <dialog class="case"> opened by [data-modal].
(function () {
  function setupCarousel(root) {
    var track = root.querySelector('.carousel-track');
    var slides = track.querySelectorAll('.carousel-slide');
    var cur = root.querySelector('[data-current]');
    var prev = root.querySelector('[data-prev]');
    var next = root.querySelector('[data-next]');
    root.querySelector('[data-total]').textContent = slides.length;

    function index() { return Math.round(track.scrollLeft / track.clientWidth); }
    function go(i) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      var smooth = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      track.scrollTo({ left: i * track.clientWidth, behavior: smooth ? 'smooth' : 'auto' });
    }
    function update() {
      var i = index();
      cur.textContent = i + 1;
      prev.disabled = i === 0;
      next.disabled = i === slides.length - 1;
    }
    prev.addEventListener('click', function () { go(index() - 1); });
    next.addEventListener('click', function () { go(index() + 1); });
    track.addEventListener('scroll', function () { window.requestAnimationFrame(update); });
    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(index() + 1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); go(index() - 1); }
    });
    root.reset = function () { track.scrollLeft = 0; update(); };
    update();
  }

  function close(d) {
    if (!d.open || d.classList.contains('is-closing')) return;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) { d.close(); return; }
    d.classList.add('is-closing');
    setTimeout(function () { d.classList.remove('is-closing'); d.close(); }, 180);
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('dialog.case').forEach(function (d) {
      var c = d.querySelector('[data-carousel]');
      if (c) setupCarousel(c);
      d.addEventListener('click', function (e) {
        if (e.target === d || e.target.closest('[data-close]')) close(d); // backdrop or close button
      });
      d.addEventListener('cancel', function (e) { e.preventDefault(); close(d); }); // Esc
      d.addEventListener('close', function () {
        document.documentElement.classList.remove('modal-open');
        if (d._opener) d._opener.focus();
      });
    });
    document.querySelectorAll('[data-modal]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var d = document.getElementById(btn.getAttribute('data-modal'));
        if (!d || !d.showModal) return;
        d._opener = btn;
        var c = d.querySelector('[data-carousel]');
        d.showModal();
        if (c && c.reset) c.reset();
        document.documentElement.classList.add('modal-open');
        d.querySelector('.case-close').focus();
      });
    });
  });
})();
