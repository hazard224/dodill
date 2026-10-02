// Portfolio: organize rows by project (original order), client, or type of solution.
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var bar = document.querySelector('.sort');
    var list = document.querySelector('section.solutions');
    if (!bar || !list) return;
    var rows = Array.prototype.slice.call(list.querySelectorAll('details.fix'));
    var anchor = rows[0].previousElementSibling; // column header row
    var KEY = { client: 'data-client', type: 'data-type' };

    function apply(mode) {
      list.querySelectorAll('.group-head').forEach(function (h) { h.remove(); });
      var after = anchor;
      if (mode === 'project') {
        rows.forEach(function (r) { after.after(r); after = r; });
      } else {
        var groups = [], seen = {};
        rows.forEach(function (r) {
          var g = r.getAttribute(KEY[mode]);
          if (!seen[g]) { seen[g] = []; groups.push(g); }
          seen[g].push(r);
        });
        groups.forEach(function (g) {
          var h = document.createElement('h2');
          h.className = 'group-head';
          h.innerHTML = g + ' <span>' + seen[g].length + '</span>';
          after.after(h); after = h;
          seen[g].forEach(function (r) { after.after(r); after = r; });
        });
      }
      bar.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', b.getAttribute('data-sort') === mode ? 'true' : 'false');
      });
      try { localStorage.setItem('portfolioSort', mode); } catch (e) {}
    }

    bar.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-sort]');
      if (b) apply(b.getAttribute('data-sort'));
    });
    var saved = null;
    try { saved = localStorage.getItem('portfolioSort'); } catch (e) {}
    if (saved && saved !== 'project') apply(saved);
  });
})();
