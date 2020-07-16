from django.shortcuts import render
from . import services

def tasks(request):
    login = request.session.get('login')
    user = services.getUserWithLogin("Manager", login)

    datacontext = {"firstname": user.firstname, "lastname": user.lastname}
    return render(request, "personalarea/tasks.html", context=datacontext)
