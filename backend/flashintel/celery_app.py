from celery import Celery

celery_app = Celery(
    'flashintel',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery_app.task
def ping():
    return 'pong'
