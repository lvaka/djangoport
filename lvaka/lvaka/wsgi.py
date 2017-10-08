"""
WSGI config for lvaka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
from whitenoise.django import DjangoWhiteNoise
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lvaka.settings")

application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application
application = DjangoWhiteNoise(application)