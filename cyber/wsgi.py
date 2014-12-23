"""
WSGI config for cyber project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
import os.path
import django.core.handlers.wsgi
sys.path.append('/var/www/project/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cyber.settings")

from django.core.wsgi import get_wsgi_application
application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
