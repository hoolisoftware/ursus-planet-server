import os

from celery import Celery
from celery.schedules import crontab
from django.contrib.auth import get_user_model


# User = get_user_model()


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()




@app.task
def test():
    print('lol')


@app.task
def send_notifications(period: str):
    pass

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'notifications-hour': {
        'task': 'tasks.test',
        'schedule': 10,
    },
    'notifications-day': {
        'task': 'tasks.test',
        'schedule': 10,
    },
    'notifications-week': {
        'task': 'tasks.test',
        'schedule': 10,
    },
    'notifications-month': {
        'task': 'tasks.test',
        'schedule': 10,
    },
}

app.conf.timezone = 'UTC'