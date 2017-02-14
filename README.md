# PoC of remote worker for Flask with Celery
Using Celery worker on separate code base. Flask app uses `celery.send_task` to submit job to celery worker.

Running with `docker-compose`

```
docker-compose build
docker-compose up
```

Flask app will serve on port `5000`. Load URI `/add/4/7`, it should create a task and return an id. Check status of id hit URI `/status/:id`.
This Poc includes [flower](http://flower.readthedocs.org) server to monitor the celery worker, its serve on port `5555`
