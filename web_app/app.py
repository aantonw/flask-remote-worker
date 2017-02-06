import os
from flask import Flask, url_for
from celery import Celery
import celery.states as states

env = os.environ
app = Flask(__name__)

app.config.update(dict(
    CELERY_BROKER_URL=env.get('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
    CELERY_RESULT_BACKEND=env.get(
        'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0'),
))

celery = Celery(
    'tasks',
    broker=env.get('CELERY_BROKER_URL', 'redis://localhost:6379/0'),
    backend=env.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
)


@app.route('/add/<int:one>/<int:two>', methods=['GET'])
def index(one, two):
    task = celery.send_task('mytasks.add', args=[one, two], kwargs={})
    return "<a href='{url}'>check status of {id}</a>".format(
        id=task.id,
        url=url_for('check_tasks', id=task.id, _external=True)
    )


@app.route('/check/<id>')
def check_tasks(id):
    res = celery.AsyncResult(id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)

if __name__ == '__main__':
    app.run(
        debug=env.get('APP_DEBUG', True),
        port=int(env.get('APP_PORT', 5000)),
        host=env.get('APP_HOST', '0.0.0.0')
    )
