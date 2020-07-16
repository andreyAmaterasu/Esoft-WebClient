from .models import Useraccount

class MyBackend(object):
    def authenticate(login=None, password=None):
        user = Useraccount.objects.get(login = login)
        return user