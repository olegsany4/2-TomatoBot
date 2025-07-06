# TomatoBot — Telegram Pomodoro Bot

## Описание

Асинхронный Telegram-бот для продуктивности по Pomodoro с поддержкой проектов, задач, геймификации, групп, кастомизации и аналитики.

## Быстрый старт

1. Клонируйте репозиторий
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Заполните .env (BOT_TOKEN, DATABASE_URL)
4. Запустите бота:
   ```bash
   python pomodoro_bot/bot.py
   ```

## Основные команды
- `/start` — начать Pomodoro
- `/pause` — пауза
- `/skipbreak` — пропустить отдых
- `/settings` — настройки
- `/newproject` — создать проект
- `/newtask` — создать задачу
- `/focus` — выбрать задачу
- `/done` — завершить задачу
- `/tasks` — список задач
- `/projects` — список проектов
- `/forest` — ваш лес
- `/stats` — статистика
- `/creategroup` — создать группу
- `/joingroup` — вступить в группу
- `/groupstats` — статистика группы
- `/leaderboard` — топ-10
- `/plan` — задачи на день
- `/dailyreminder` — напоминание
- `/theme` — смена темы
- `/guide` — интерактивный гайд

## Тесты

- Юнит-тесты: `pytest pomodoro_bot/handlers/tests/`

## Лицензия
MIT
