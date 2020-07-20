"""Services for PersonArea"""
from .models import Manager, Performer

def getUserWithLogin(login):
    try:
        return Performer.objects.get(login=login)
    except Performer.DoesNotExist:
        return Manager.objects.get(login=login)

def getAllUsersOfType(type_of_user):
    if type_of_user == "Performer":
        return Performer.objects.all()
    elif type_of_user == "Manager":
        return Manager.objects.all()
