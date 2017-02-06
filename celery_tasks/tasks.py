import os
from celery import Celery
from time import sleep

env = os.environ
app = Celery(
    'tasks',
    broker=env.get('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
    backend=env.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
)


@app.task(name='mytasks.add')
def add(x, y):
    sleep(7)  # mimic long process with sleep
    return x + y
