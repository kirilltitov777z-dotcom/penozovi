// Penozovi plugin: Часы чтения
(() => {
  const start = Date.now();
  window.__penozoviReadingSession = { startedAt: start, minutes: 0 };
  setInterval(() => {
    window.__penozoviReadingSession.minutes = Math.floor((Date.now() - start) / 60000);
  }, 60000);
})();
