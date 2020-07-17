from django.shortcuts import render
from django.http import HttpResponse
from . import services

def tasks(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        datacontext = {"firstname": user.firstname, "lastname": user.lastname}
        return render(request, "personalarea/tasks.html", context=datacontext)

def performers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        datacontext = {"firstname": user.firstname, "lastname": user.lastname}
        return render(request, "personalarea/performers.html", context=datacontext)

def managers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        datacontext = {"firstname": user.firstname, "lastname": user.lastname}
        return render(request, "personalarea/managers.html", context=datacontext)
