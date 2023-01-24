import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')

app = Celery('ModelProject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_5_seconds': {
        'task': 'NewsPortal.tasks.printer',
        'schedule': 5,
        'args': (5, ),
    },
}

