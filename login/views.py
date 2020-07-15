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

        useraccount = services.getUseraccountWhithLogin("Useraccount", entered_login)
        if useraccount:
            if useraccount[0].login == entered_login and useraccount[0].password == entered_password:
                useraccount[0].datetimeauthorized = datetime.now()
                useraccount[0].save()
                return render(request, "personalarea/index.html")
        userform = UserForm()
        return render(request, "login/login.html", {"form": userform, "error": True})
    else:
        userform = UserForm()
        return render(request, "login/login.html", {"form": userform})
