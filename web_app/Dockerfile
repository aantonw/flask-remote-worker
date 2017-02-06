FROM python:2.7-alpine
MAINTAINER Anton Wahyu <mail@anton.web.id>

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && mkdir -p /app
WORKDIR /app

COPY ./app.py /app/app.py

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0

ENV APP_HOST 0.0.0.0
ENV APP_PORT 5000
ENV APP_DEBUG true

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["/app/app.py"]



