// Smooth open/close for the portfolio rows (<details class="fix">).
// Without JS, or with reduced motion, the rows still open and close instantly.
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !Element.prototype.animate) return;

  var OPEN_MS = 380, CLOSE_MS = 260;
  var EASE_OPEN = 'cubic-bezier(.2,.7,.2,1)', EASE_CLOSE = 'cubic-bezier(.4,0,.6,1)';

  function setup(d) {
    var summary = d.querySelector('summary');
    var body = d.querySelector('.fix-body');
    if (!summary || !body) return;
    var anim = null;

    function finish(open) {
      anim = null;
      d.classList.remove('is-closing', 'is-opening');
      body.style.height = body.style.overflow = '';
      if (!open) d.open = false;
    }

    summary.addEventListener('click', function (e) {
      e.preventDefault();
      var start = d.open ? body.getBoundingClientRect().height : 0;
      if (anim) anim.cancel();

      if (d.open && !d.classList.contains('is-closing')) {
        // close
        d.classList.add('is-closing');
        d.classList.remove('is-opening');
        body.style.overflow = 'hidden';
        anim = body.animate(
          [{ height: start + 'px', opacity: 1, transform: 'translateY(0)' },
           { height: '0px', opacity: 0, transform: 'translateY(-8px)' }],
          { duration: CLOSE_MS, easing: EASE_CLOSE });
        anim.onfinish = function () { finish(false); };
      } else {
        // open (pick up from the current height if a close was in progress)
        var wasClosing = d.classList.contains('is-closing');
        var from = wasClosing ? start : 0;
        d.classList.remove('is-closing');
        d.classList.add('is-opening');
        d.open = true;
        body.style.overflow = 'hidden';
        var end = body.scrollHeight;
        anim = body.animate(
          [{ height: from + 'px', opacity: wasClosing ? 0.4 : 0, transform: 'translateY(-8px)' },
           { height: end + 'px', opacity: 1, transform: 'translateY(0)' }],
          { duration: OPEN_MS, easing: EASE_OPEN });
        anim.onfinish = function () { finish(true); };
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('details.fix').forEach(setup);
  });
})();
