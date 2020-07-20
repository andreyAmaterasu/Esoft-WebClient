from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import services
from .serializers import ManagerSerializer, PerformerSerializer, ManagerForPerformerSerializer
from rest_framework.renderers import JSONRenderer
from .models import Manager, Performer
from django.core import serializers
from django.forms.models import model_to_dict

def tasks(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        data_context = {"user_context": serialized_user}
        return render(request, "personalarea/tasks.html", context=data_context)

def performers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        managers_persormers = {}
        managers_persormers["performers"] = services.getAllUsersOfType("Performer")

        managers_login = []
        for performer in managers_persormers["performers"]:
            if performer.manager.login not in managers_login:
                managers_login.append(performer.manager.login)

        queryset_manager = Manager.objects.filter(login__in=managers_login)
        
        managers_persormers["managers"] = queryset_manager
       
        serialized_managers_performers = ManagerForPerformerSerializer(managers_persormers).data

        serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        data_context = {"managers_performers_context": serialized_managers_performers, "user_context": serialized_user}
        return render(request, "personalarea/performers.html", context=data_context)
