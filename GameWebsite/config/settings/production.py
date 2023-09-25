from GameWebsite.config.settings.common import *
import os
import dj_database_url
import ast

# Access the environment variables using 'os.environ' in your Django settings.py
SECRET_KEY = os.environ.get('SECRET_KEY')  # Django SECRET_KEY


DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
# Access the Database Configuration
# DB_NAME = os.environ.get('DB_NAME')
# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')
# DB_HOST = os.environ.get('DB_HOST')
# DB_PORT = os.environ.get('DB_PORT')

# Debug Mode
DEBUG = os.environ.get('DEBUG')

# Retrieve the ALLOWED_HOSTS value from the environment variable
# in string format and change it to original data type

# ALLOWED_HOSTS = ast.literal_eval(os.environ.get('ALLOWED_HOSTS'))
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Email Configuration
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')