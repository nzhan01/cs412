"""
WSGI config for cs412 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the PYTHONPATH
sys.path.insert(0, '/home/ugrad/nzhan01/webapps/django/cs412')

# Activate your virtual environment to allow django-allauth to work
activate_env = '/home/ugrad/nzhan01/webapps/django/cs412/venv/bin/activate_this.py'
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs412.settings')

application = get_wsgi_application()
