release: python manage.py makemigrations & python manage.py migrate --settings=website.settings & python manage.py collectstatic
web: gunicorn website.wsgi --log-file -
