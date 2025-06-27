import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_task_bot.settings')
app = Celery('django_task_bot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()