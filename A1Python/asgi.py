"""
ASGI config for A1Python project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file_path, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A1Python.settings')

application = get_asgi_application()
