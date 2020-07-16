""" Business logic is here """
from datetime import datetime
from .models import Useraccount

def login_user(login, password):
    """ User authentication using login and password """
    try:
        user = Useraccount.objects.get(login=login, password=password)
        user.datetimeauthorized = datetime.now()
        user.save()
        return user
    except Useraccount.DoesNotExist:
        return None
