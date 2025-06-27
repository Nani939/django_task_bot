# Django Task Bot Project

A Django REST Framework-based backend project with:
- User Registration API
- Token Authentication
- Celery + Redis background task
- Telegram Bot Integration
- .env configuration and secure setup

## Features
- `/api/register/`: Register a new user
- `/api/profile/`: Get user profile (token protected)
- Telegram message sent on successful registration
- Celery for async processing

## Setup Instructions

```bash
git clone https://github.com/Nani939/django_task_bot.git
cd django_task_bot
cp .env.example .env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Start Celery Worker

```bash
celery -A django_task_bot worker --loglevel=info
```

## Run Redis
Install and run Redis server on localhost before starting Celery.

## API Usage
- `POST /api/register/`
- `GET /api/profile/` (Requires Token)

