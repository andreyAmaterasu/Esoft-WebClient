from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import services
from .serializers import ManagerSerializer
from rest_framework.renderers import JSONRenderer
from .models import Manager
from django.core import serializers
from django.forms.models import model_to_dict

class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

def tasks(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        datacontext = {"firstname": user.firstname, "lastname": user.lastname}
        return render(request, "personalarea/tasks.html", {"context": datacontext})

def performers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        datacontext = {"firstname": user.firstname, "lastname": user.lastname}
        return render(request, "personalarea/performers.html", {"context": datacontext})

def managers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        queryset = Manager.objects.all()
        serializer_class = ManagerSerializer(queryset, many=True)
        serialized_data = serializer_class.data
        
        

        managers = serialized_data
        user1 = {"firstname": user.firstname, "lastname": user.lastname}
        data_context = {"managers": managers, "user": user1}
        return render(request, "personalarea/managers.html", context=data_context)
