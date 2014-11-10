from .base import *

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = 'replace me'
NEVERCACHE_KEY = 'replace me'

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "{{cookiecutter.project_name}}_db3",
        # Not used with sqlite3.
        "USER": "{{cookiecutter.project_name}}",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "/containers/{{cookiecutter.container_id}}/db.pg",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
