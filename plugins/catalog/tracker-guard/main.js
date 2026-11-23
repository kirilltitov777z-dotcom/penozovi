// Penozovi plugin: Страж трекеров+
(() => {
  const extraBlocked = ['pixel.quantserve.com', 'bat.bing.com', 'analytics.tiktok.com'].join('|');
  // Демонстрация: расширенный список правил. Реальная фильтрация живёт в ядре браузера.
  window.__penozoviExtraBlockedHosts = extraBlocked;
})();
