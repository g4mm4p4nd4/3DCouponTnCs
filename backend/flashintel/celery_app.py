import os
from celery import Celery

celery_app = Celery("flashintel")
celery_app.conf.broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
celery_app.conf.result_backend = os.getenv(
    "CELERY_RESULT_BACKEND", "redis://redis:6379/0"
)
