import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    debug = os.getenv('DEBUG', True)
    if debug:  # local
        os.environ.setdefault('DATABASE_URL',
                              'sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
