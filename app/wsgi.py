import os
import sys
from django.core.wsgi import get_wsgi_application

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, current_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = get_wsgi_application()
