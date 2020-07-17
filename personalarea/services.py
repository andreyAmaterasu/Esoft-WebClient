"""Services for PersonArea"""
from .models import Manager, Performer

def getUserWithLogin(login):
    try:
        return Performer.objects.get(login=login)
    except Performer.DoesNotExist:
        return Manager.objects.get(login=login)
