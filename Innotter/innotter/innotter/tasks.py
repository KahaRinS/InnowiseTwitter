from innotter.celery import app
import time
from celery import shared_task

@shared_task
def my_task():
    return 'hi'