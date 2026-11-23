// Penozovi plugin: Тёплый вечер
(() => {
  const style = document.createElement('style');
  style.id = 'penozovi-night-shift';
  style.textContent = `
    html { filter: sepia(0.18) saturate(1.05) brightness(0.92); }
    body { transition: filter 240ms ease; }
  `;
  (document.head || document.documentElement).appendChild(style);
})();
