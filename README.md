# FreelanceBoard

Биржа фриланса на Django и PostgreSQL.

## Требования

- Python 3.13 (проверено; подходит 3.10 и выше)
- PostgreSQL 15 и выше, запущенная служба

## Развёртывание

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Заполните `.env` своими значениями (пароль БД, SECRET_KEY), создайте базу:

```
psql -U postgres -c "CREATE DATABASE freelanceboard;"
```

Затем:

```
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Проверка

- http://127.0.0.1:8000/ — главная страница
- http://127.0.0.1:8000/health/ — служебный маршрут (JSON)
- http://127.0.0.1:8000/api/ping/ — тестовый API-маршрут
- http://127.0.0.1:8000/admin/ — админ-панель

## Структура

- `config/` — настройки и корневые маршруты
- `accounts/` — пользователи и авторизация
- `marketplace/` — заказы, отклики, отзывы
- `assistant/` — заготовка модуля помощника
- `api/` — служебные JSON-маршруты
- `templates/`, `static/`, `media/` — шаблоны, статика, загружаемые файлы
