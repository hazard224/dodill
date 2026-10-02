// Google Analytics, loaded only after the visitor accepts.
// Same measurement ID and consent key as the original dodill homepage,
// so returning visitors keep the choice they already made.
(function () {
  var ID = 'G-Z7GDFC656N';
  var KEY = 'cookieConsent';

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return 'declined'; } }
  function write(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  function load() {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', ID);
  }

  function banner(privacyHref) {
    var b = document.createElement('div');
    b.className = 'consent';
    b.setAttribute('role', 'region');
    b.setAttribute('aria-label', 'Cookie consent');
    b.innerHTML =
      '<p>This site uses Google Analytics to see which pages get used. <a href="' + privacyHref + '">Privacy policy</a></p>' +
      '<div class="consent-actions"><button type="button" class="btn btn-primary" data-v="accepted">Accept</button>' +
      '<button type="button" class="btn" data-v="declined">Decline</button></div>';
    b.addEventListener('click', function (e) {
      var v = e.target.getAttribute && e.target.getAttribute('data-v');
      if (!v) return;
      write(v);
      b.remove();
      if (v === 'accepted') load();
    });
    document.body.appendChild(b);
  }

  var choice = read();
  if (choice === 'accepted') { load(); return; }
  if (choice === null) {
    var privacy = (document.currentScript && document.currentScript.getAttribute('data-privacy')) || 'privacy.html';
    document.addEventListener('DOMContentLoaded', function () { banner(privacy); });
  }
})();
