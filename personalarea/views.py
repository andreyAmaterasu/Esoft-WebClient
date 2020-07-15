from django.shortcuts import render
from . import services

def index(request):
    login = request.GET.get("login")

    user = services.getUserWithLogin("Manager", login)

    datacontext = {"firstname": user.firstname, "lastname": user.lastname}
    return render(request, "personalarea/base.html", context=datacontext)
