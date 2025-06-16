from celery import Celery
import os

BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
BACKEND_URL = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/1')

celery_app = Celery('flashintel', broker=BROKER_URL, backend=BACKEND_URL)

celery_app.conf.update(
    task_track_started=True,
)
