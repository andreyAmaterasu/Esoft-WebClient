from .models import Useraccount

def getUseraccounts():
    return Useraccount.objects.all()