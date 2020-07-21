from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import services
from .serializers import ManagerSerializer, PerformerSerializer, TaskSerializer, ManagerForPerformerSerializer, TaskPerformerManagerSerializer
from rest_framework.renderers import JSONRenderer
from .models import Manager, Performer, Task
from django.core import serializers
from django.forms.models import model_to_dict

def tasks(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        login = request.session.get('login')
        user = services.getUserWithLogin(login)

        try:
            # performer = Performer.objects.get(login=login)
            # tasks = Task.objects.filter(taskperformer=login)
            # manager = performer.manager

            tasks_performer_manager = {}
            tasks_performer_manager["tasks"] = Task.objects.filter(taskperformer=login)
            tasks_performer_manager["performer"] = Performer.objects.get(login=login)
            tasks_performer_manager["manager"] = tasks_performer_manager["performer"].manager

            serialized_tasks_performer_manager = TaskPerformerManagerSerializer(tasks_performer_manager).data

            # serialized_task = TaskSerializer(tasks, many=True)
            # serialized_performer = PerformerSerializer(performer)
            # serialized_manager = ManagerSerializer(tasks_performer_manager["manager"])

        except Performer.DoesNotExist:
            Manager.objects.get(login=login)

        serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        data_context = {"tasks_performer_manager_context": serialized_tasks_performer_manager, "user_context": serialized_user}
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
