# 🍥 Penozovi Browser

**Penozovi** — мобильный браузер, собранный на базе [Candy Browser](https://github.com/sk2andy/candy-browser), но переделанный под телефон и под наш стиль.

Это форк: исходная архитектура, жесты, приватность и WebView/Gecko остаются от Candy Browser, а брендинг, иконка, тема и система плагинов — наши.

## Что изменилось

- **Новое имя и иконка.** Penozovi вместо Candy Browser; иконка — розовый «лепестковый» знак с другим символом (не `π`).
- **Одна тема — Material.** Material Expressive включена по умолчанию и является единственной темой интерфейса. Никаких «внешних» тем и переключателей дизайна.
- **Плагины и магазин.** Появился формат манифеста плагина, реестр плагинов и магазин, который собирается GitHub Actions.
- **Сборка через GitHub Actions.** APK собирается и публикуется автоматически в CI — телефон ничего собирать не должен.

## Возможности (от Candy Browser)

- Жестовое управление и Material 3 Expressive.
- Локальные инструменты приватности: блокировка трекеров, фильтры, правила.
- Вкладки, RSS-ленты, офлайн-чтение, загрузки, синхронизация.
- Работа через системный WebView или GeckoView (сборки `foss`).

## Сборка

- `.github/workflows/penozovi-build.yml` — сборка debug APK на каждый push и PR, артефакт прикрепляется к запуску.
- `.github/workflows/penozovi-release.yml` — сборка release APK по тегу `v*` и публикация GitHub Release.
- `.github/workflows/plugin-store.yml` — проверка манифестов плагинов и публикация каталога магазина.

Локально (если нужен Android SDK):

```bash
./gradlew :app:assembleDebug
```

## Плагины

Каталог лежит в [`plugins/catalog/`](plugins/catalog/), формат описан в [`docs/PLUGINS.md`](docs/PLUGINS.md), а собранный магазин — в [`store/`](store/).

Чтобы добавить плагин: создайте JSON по [`manifest.schema.json`](plugins/manifest.schema.json) в `plugins/catalog/` и откройте PR. Workflow проверит манифест и обновит `store/index.json`.

## Благодарности

Основа — [Candy Browser](https://github.com/sk2andy/candy-browser) от [@sk2andy](https://github.com/sk2andy). Спасибо оригинальному проекту за код и дизайн. Penozovi — независимый ребрендинг и развитие.

## Лицензия

Наследует лицензию оригинального репозитория. См. [LICENSE](LICENSE) и [LICENSING.md](LICENSING.md).
