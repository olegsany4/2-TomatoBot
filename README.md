# TomatoBot — Telegram Pomodoro Bot

## Описание
Асинхронный Telegram-бот для продуктивности по Pomodoro с поддержкой проектов, задач, геймификации, групп, кастомизации и аналитики.

---

## 📁 Архитектура

```
/2 TomatoBot
├── bot.py
├── config.py
├── requirements.txt
├── Dockerfile
├── README.md
├── WHAT_WAS_DONE.txt
├── db
│   ├── models.py
│   └── session.py
├── handlers
│   ├── gamification.py
│   ├── guide.py
│   ├── groups.py
│   ├── pomodoro.py
│   ├── projects.py
│   ├── settings.py
│   ├── tasks.py
│   └── tests
│       ├── test_parallel_users.py
│       ├── test_tasks.py
│       └── test_timer.py
├── pomodoro_bot
│   └── handlers
│       └── tests
│           └── test_timer.py
├── services
│   ├── audio.py
│   ├── forest.py
│   ├── reminders.py
│   ├── scheduler.py
│   ├── theme.py
│   └── timer.py
├── static
│   └── themes
│       ├── dark.json
│       ├── forest.json
│       └── light.json
├── utils
│   ├── helpers.py
│   └── scheduler.py
└── .vscode
    └── settings.json
```


```
/2 TomatoBot
├── bot.py
├── config.py
├── requirements.txt
├── Dockerfile
├── README.md
├── WHAT_WAS_DONE.txt
├── db
│   ├── models.py
│   └── session.py
├── handlers
│   ├── gamification.py
│   ├── guide.py
│   ├── groups.py
│   ├── pomodoro.py
│   ├── projects.py
│   ├── settings.py
│   ├── tasks.py
│   └── tests
│       ├── test_parallel_users.py
│       ├── test_tasks.py
│       └── test_timer.py
├── pomodoro_bot
│   └── handlers
│       └── tests
│           └── test_timer.py
├── services
│   ├── audio.py
│   ├── forest.py
│   ├── reminders.py
│   ├── scheduler.py
│   ├── theme.py
│   └── timer.py
├── static
│   └── themes
│       ├── dark.json
│       ├── forest.json
│       └── light.json
├── utils
│   ├── helpers.py
│   └── scheduler.py
└── .vscode
    └── settings.json
```

- **handlers/** — обработчики команд Telegram
- **services/** — бизнес-логика (таймер, лес, темы, напоминания)
- **db/** — модели и сессии SQLAlchemy
- **utils/** — вспомогательные функции и планировщик
- **static/** — темы оформления

---

## 🔧 Технологии
- **Язык:** Python 3.11+
- **Фреймворк:** python-telegram-bot[asyncio] >= 20.0
- **ORM:** SQLAlchemy >= 2.0 (async)
- **БД:** SQLite (по умолчанию, рекомендуется PostgreSQL для продакшена)
- **Тесты:** pytest
- **Docker:** есть Dockerfile
- **CI/CD:** отсутствует
- **Линтеры:** отсутствуют
- **.env:** через python-dotenv
- **Асинхронность:** да (async/await)
- **Парадигмы:** монолит, REST-like команды, сервисный слой

---

## Проблемы и технический долг
- Нет полноценной обработки ошибок (try/except, fallback)
- Нет валидации пользовательского ввода (SQL-инъекции, XSS маловероятны, но возможны ошибки)
- Используется SQLite, нет миграций (Alembic)
- Нет аннотаций типов, слабая документация
- Нет DI-контейнера, нет паттернов CQRS/DDD
- Нет CI/CD, нет линтеров, покрытие тестами минимальное
- Нет graceful shutdown, retry-механизмов

**Проблемные места:**
- `handlers/tasks.py`: отсутствие валидации и try/except при работе с БД
- `services/timer.py`: нет обработки ошибок при старте/паузе таймера
- `db/models.py`: нет валидации данных, нет аннотаций типов

---

## Сильные стороны
- Асинхронная архитектура, высокая модульность
- Четкое разделение слоев (handlers, services, db)
- Простота расширения (новые сервисы, команды)
- Использование ORM и сервисного слоя
- Легкий запуск и настройка (Docker, .env)

---

## Рекомендации и roadmap

### Приоритетные доработки
| Задача | Приоритет | Сложность |
|--------|-----------|-----------|
| Внедрить PostgreSQL и Alembic | high | medium |
| Добавить обработку ошибок и валидацию | high | low/medium |
| Ввести аннотации типов и docstrings | medium | low |
| Покрыть тестами бизнес-логику | high | medium |
| Внедрить CI/CD (GitHub Actions) | medium | medium |
| Добавить линтеры (flake8, black) | medium | low |
| Улучшить документацию | low | low |
| Реализовать graceful shutdown, retry | medium | medium |

### Roadmap
- **30 дней:**
  - Внедрить PostgreSQL, Alembic, добавить миграции
  - Покрыть тестами основные сервисы (timer, tasks, projects)
  - Ввести обработку ошибок и базовую валидацию
- **60 дней:**
  - Внедрить CI/CD, линтеры, pre-commit хуки
  - Добавить аннотации типов, docstrings
  - Улучшить документацию (пример .env, схемы)
- **90 дней:**
  - Реализовать retry, graceful shutdown
  - Перевести на DI-контейнер (например, dependency-injector)
  - Добавить интеграционные тесты, покрыть edge-cases

### Альтернативы
- Вместо SQLite использовать PostgreSQL (более надежно и масштабируемо)
- Вместо ручной обработки ошибок — использовать middleware/logging
- Вместо монолита — рассмотреть микросервисы при росте нагрузки

---

## Быстрый старт

1. Клонируйте репозиторий
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Заполните .env (BOT_TOKEN, DATABASE_URL)
4. Запустите бота:
   ```bash
   python bot.py
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
- Юнит-тесты: `pytest handlers/tests/`

## Лицензия
MIT
