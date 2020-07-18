from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import services
from .serializers import ManagerSerializer
from rest_framework.renderers import JSONRenderer
from .models import Manager
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

        serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        data_context = {"user_context": serialized_user}
        return render(request, "personalarea/performers.html", context=data_context)

def managers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        queryset = Manager.objects.all()
        serializer_class = ManagerSerializer(queryset, many=True)
        serialized_manager = serializer_class.data

        serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        data_context = {"managers_context": serialized_manager, "user_context": serialized_user}
        return render(request, "personalarea/managers.html", context=data_context)
