FROM python:3.8

ENV DEBUG=TRUE

WORKDIR /site

COPY requirements.txt ./

RUN pip install -U pip && \
    pip install -r requirements.txt

EXPOSE 8080

CMD python manage.py runserver 0.0.0.0:8080
