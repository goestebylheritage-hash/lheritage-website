// Startbeeld: wisselt de foto's elke 6 seconden met een zachte overgang.
(function () {
  var box = document.querySelector('[data-slideshow]');
  if (!box) return;
  var slides = box.querySelectorAll('.slide');
  var dots = box.querySelectorAll('.slide-dots button');
  if (slides.length < 2) return;
  var current = 0, timer = null;
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function show(n) {
    slides[current].classList.remove('is-active');
    dots[current].removeAttribute('aria-current');
    current = (n + slides.length) % slides.length;
    var img = slides[current];
    if (img.loading === 'lazy') img.loading = 'eager';
    img.classList.add('is-active');
    dots[current].setAttribute('aria-current', 'true');
  }
  function start() { if (!still) { stop(); timer = setInterval(function () { show(current + 1); }, 6000); } }
  function stop() { if (timer) clearInterval(timer); timer = null; }

  dots.forEach(function (dot, i) { dot.addEventListener('click', function () { show(i); start(); }); });
  // Volgende foto alvast laden, zodat de overgang niet hapert.
  window.addEventListener('load', function () { slides.forEach(function (s) { s.loading = 'eager'; }); });
  document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
  start();
})();
