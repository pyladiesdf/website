release: python manage.py makemigrations & python manage.py migrate --settings=website.settings
web: gunicorn website.wsgi --log-file -
