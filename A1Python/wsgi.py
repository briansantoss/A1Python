"""
WSGI config for A1Python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file_path, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A1Python.settings')

application = get_wsgi_application()
