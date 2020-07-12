""" View - receiving a request, processing, sending a response """
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from . import services

def login(request):
    """ authorization """
    if request.method == "POST":
        entered_login = request.POST.get("login")
        entered_password = request.POST.get("password")

        useraccounts = services.getUseraccounts()
        for useraccount in useraccounts:
            if useraccount.login == entered_login:
                useraccount.datetimeauthorized = datetime.now()
                useraccount.save()
                return HttpResponse("Вход выполнен")
        return HttpResponse("ERROR!!")
    else:
        userform = UserForm()
        return render(request, "login/login.html", {"form": userform})
