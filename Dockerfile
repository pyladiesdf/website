FROM python:3.8

ENV DEBUG=TRUE \
    MODE=docker

EXPOSE 8080

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -U pip && \
    pip install -r requirements.txt

COPY . .

ENTRYPOINT python manage.py runserver 0.0.0.0:8080
