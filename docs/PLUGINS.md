# Плагины Penozovi

Плагин — это небольшой JSON-манифест плюс (опционально) файлы контент-скрипта. Магазин плагинов строится из каталога `plugins/catalog/` GitHub Actions.

## Манифест

Минимальный пример:

```json
{
  "id": "dev.penozovi.plugin.night-shift",
  "name": "Тёплый вечер",
  "version": "1.0.0",
  "author": "Penozovi",
  "description": "Мягкий тёплый фильтр для ночного чтения.",
  "category": "appearance",
  "icon": "🌙",
  "permissions": ["content"],
  "entry": "main.js",
  "minBrowserVersion": "1.0.0"
}
```

Обязательные поля: `id`, `name`, `version`, `author`, `description`, `category`.
Полная схема: [`plugins/manifest.schema.json`](../plugins/manifest.schema.json).

### Категории

`appearance`, `privacy`, `productivity`, `media`, `feeds`, `other`.

### Разрешения

`content` — доступ к контент-скрипту, `storage` — локальное хранилище, `network` — сетевые запросы.

## Как опубликовать

1. Форкните репозиторий.
2. Добавьте папку `plugins/catalog/<id>/` с `manifest.json` и (если нужно) `main.js`.
3. Откройте Pull Request в `main`.
4. Workflow `plugin-store.yml` проверит манифест по схеме и пересоберёт `store/index.json`.
5. После мержа плагин появится в магазине.

## Как установить

В браузере: **Настройки → Плагины → Магазин**, либо вручную добавьте манифест по ссылке на raw-файл из репозитория.

## Магазин

Статическая страница магазина лежит в `store/index.html`. Она читает `store/index.json`, который генерируется CI. Каталог также копируется в `app/src/main/assets/penozovi_plugins/store.json`, чтобы браузер мог показывать его офлайн.
