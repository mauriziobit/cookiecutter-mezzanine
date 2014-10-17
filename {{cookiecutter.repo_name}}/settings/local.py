from .base import *

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "05e712b9-1d2c-4b01-b255-e6719fc475b860eb2471-f58f-4259-99e8-b7df9fc510c9d34591fe-a252-45f7-8f15-47d31ca125cd"
NEVERCACHE_KEY = "6b069d3b-705d-40e2-8db8-a1a0dab819ccf6083c2f-3213-445d-8668-6e31d6c4904dd42c837f-bd6b-494c-b6f1-1a8b2b3e4249"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "{{cookiecutter.environment}}.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
