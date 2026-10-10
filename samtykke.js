/*
 * Samtykke til besøksstatistikk på getbusted.no (ekomloven § 3-15 og GDPR art. 6 nr. 1 a).
 * Metricool lastes bare etter at besøkende har trykket «Godta». Uten valg, eller ved «Avslå», sendes ingenting.
 * Valget lagres i nettleseren (localStorage «gb-samtykke») og kan endres via lenken «Informasjonskapsler»
 * i bunnen (alle elementer med data-samtykke). Les mer: /informasjonskapsler/
 */
(function () {
  var KEY = 'gb-samtykke';
  var VERSION = 1; // Øk når formålet eller leverandøren endres, så alle blir spurt på nytt.
  var METRICOOL_HASH = '609b5eda0e3d6e76f8ce1f20d947c406';

  function read() {
    try { var v = JSON.parse(localStorage.getItem(KEY) || 'null'); return v && v.v === VERSION ? v : null; } catch (e) { return null; }
  }
  function save(ok) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: VERSION, stats: ok, at: new Date().toISOString() })); } catch (e) { /* lagres ikke */ }
  }

  var loaded = false;
  function loadStats() {
    if (loaded) return; loaded = true;
    var s = document.createElement('script');
    s.src = 'https://tracker.metricool.com/resources/be.js';
    s.onload = function () { try { window.beTracker.t({ hash: METRICOOL_HASH }); } catch (e) { /* ingen statistikk */ } };
    document.head.appendChild(s);
  }

  var box = null, lastFocus = null;
  function close() {
    if (box) { box.remove(); box = null; }
    if (lastFocus && document.contains(lastFocus)) lastFocus.focus();
  }
  function choose(ok) {
    var before = read();
    save(ok);
    close();
    if (ok) loadStats();
    else if (before && before.stats) location.reload(); // trekker samtykket: last siden på nytt uten Metricool
  }
  function open(fromUser) {
    if (box) return;
    lastFocus = fromUser ? document.activeElement : null;
    box = document.createElement('section');
    box.className = 'consent';
    box.setAttribute('role', 'region');
    box.setAttribute('aria-label', 'Samtykke til statistikk');
    box.innerHTML =
      '<p>Vi teller besøk anonymt med Metricool. Godta? <a href="/informasjonskapsler/">Les mer</a></p>' +
      '<div class="consent-b"><button type="button" data-v="0">Avslå</button><button type="button" data-v="1">Godta</button></div>';
    box.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () { choose(b.getAttribute('data-v') === '1'); });
    });
    box.addEventListener('keydown', function (e) { if (e.key === 'Escape' && read()) close(); });
    var skip = document.querySelector('.skip'); // rett etter hopp-lenken, først i tab-rekkefølgen ellers
    document.body.insertBefore(box, skip ? skip.nextSibling : document.body.firstChild);
    if (fromUser) box.querySelector('button').focus();
  }

  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-samtykke]');
    if (t) { e.preventDefault(); open(true); }
  });

  var c = read();
  if (c && c.stats) loadStats();
  if (!c) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { open(false); });
    else open(false);
  }
})();
