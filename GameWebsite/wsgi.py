"""
WSGI config for GameWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GameWebsite.settings')

# This makes our Django application use the development.py file
# when the DJANGO_SETTINGS_MODULE environment variable is not set.
# you can change in to production by 'GameWebsite.config.settings.production'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GameWebsite.config.settings.production')

application = get_wsgi_application()
