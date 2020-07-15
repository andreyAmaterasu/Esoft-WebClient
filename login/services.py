from .models import Useraccount
from datetime import datetime

def loginUser(login, password):
    useraccount = Useraccount.objects.filter(login = login, password = password)
    if useraccount:
        useraccount[0].datetimeauthorized = datetime.now()
        useraccount[0].save()
        return True
    else:
        return False
