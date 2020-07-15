from .models import Useraccount

def getUseraccounts():
    return Useraccount.objects.all()

def getUseraccountWhithLogin(typeOfUser, login):
    if typeOfUser == "Useraccount":
        return Useraccount.objects.filter(login = login)
