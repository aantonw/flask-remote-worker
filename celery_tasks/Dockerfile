FROM python:2.7-alpine
MAINTAINER Anton Wahyu <mail@anton.web.id>

ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && mkdir tasks
WORKDIR /tasks

COPY ./tasks.py /tasks/tasks.py

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0

EXPOSE 5555


ENTRYPOINT ["celery", "-A", "tasks", "worker", "--loglevel=info"]
