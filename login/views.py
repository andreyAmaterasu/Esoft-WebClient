""" View - receiving a request, processing, sending a response """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from . import services

def login(request):
    """ authorization """
    if request.method == "POST":
        entered_login = request.POST.get("login")
        entered_password = request.POST.get("password")

        if services.loginUser(entered_login, entered_password):
            return HttpResponseRedirect("/personalarea/?login={0}".format(entered_login))
        else:
            userform = UserForm()
            return render(request, "login/login.html", {"form": userform, "error": True})
    else:
        userform = UserForm()
        return render(request, "login/login.html", {"form": userform})
