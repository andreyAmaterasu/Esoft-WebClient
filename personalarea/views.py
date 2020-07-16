from django.shortcuts import render
from . import services

def tasks(request):
    login = request.GET.get("login")

    user = services.getUserWithLogin("Manager", login)
    login = request.session.get('login')

    datacontext = {"firstname": login, "lastname": user.lastname}
    return render(request, "personalarea/tasks.html", context=datacontext)
