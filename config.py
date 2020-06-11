import os

DEFAULT_VALUES = {
    'LOG_LEVEL': 'info',

    'DB_HOST': '127.0.0.1',
    'DB_PORT': '3306',
    'DB_USER': 'root',
    'DB_PASS': 'root',
    'DB_NAME': 'py-rest'
}


def get(key):
    return os.getenv(key, DEFAULT_VALUES[key])
