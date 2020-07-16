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
        user = services.login_user(entered_login, entered_password)

        if user is not None:
            request.session['login'] = entered_login
            return HttpResponseRedirect("/personalarea/tasks")
        else:
            userform = UserForm()
            return render(request, "login/login.html", {"form": userform, "error": True})
    else:
        userform = UserForm()
        return render(request, "login/login.html", {"form": userform})
