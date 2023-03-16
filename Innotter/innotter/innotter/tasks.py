import time

from celery import shared_task

from innotter.celery import app


@shared_task
def my_task():
    print('haho')
    return True