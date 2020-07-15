"""Services for PersonArea"""
from .models import Manager

def getUserWithLogin(typeOfUser, login):
    if typeOfUser == "Manager":
        return Manager.objects.get(login = login)
