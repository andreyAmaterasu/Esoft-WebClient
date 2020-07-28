import os, sys
sys.path.append('C:\\Users\\andre\\Downloads\\OpenServer\\domains')
sys.path.append('C:\\Users\\andre\\Downloads\\OpenServer\\domains\\esoft\\env\\lib\\python3.6\\site=packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'esoft.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()