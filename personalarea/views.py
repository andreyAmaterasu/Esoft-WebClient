from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import services
from .serializers import ManagerForPerformerSerializer, TasksPerformerManagerSerializer, TasksManagerPerformersSerializer, PerformerSerializer, ManagerSerializer, TaskSerializer
from rest_framework.renderers import JSONRenderer
from .models import Manager, Performer, Task
from django.core import serializers
from django.forms.models import model_to_dict

class PerformerViewSet(ModelViewSet):
    serializer_class = PerformerSerializer
    queryset = Performer.objects.all()

class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class PerformerManagerViewSet(ModelViewSet):
    serializer_class = PerformerSerializer
    queryset = Performer.objects.all()

class TaskPerformerManagerViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

def tasks(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        # login = request.session.get('login')
        # user = services.getUserWithLogin(login)

        # serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        # user = services.getUserWithLogin(login)
        # if isinstance(user, Performer):
        #     task_performer = {}
        #     task_performer["tasks"] = Task.objects.filter(taskperformer=login)
        #     task_performer["performers"] = user
        #     task_performer["manager"] = task_performer["performers"].manager

        #     serialized_task_performer = TasksPerformerManagerSerializer(task_performer).data

        #     data_context = {"task_context": serialized_task_performer, "user_context": serialized_user}

        # else:
        #     task_manager = {}
        #     task_manager["manager"] = user
        #     task_manager["performers"] = Performer.objects.filter(manager=task_manager["manager"])
        #     task_manager["tasks"] = Task.objects.filter(taskperformer__in=task_manager["performers"])
            
        #     serialized_tasks_manager = TasksManagerPerformersSerializer(task_manager).data

        #     data_context = {"task_context": serialized_tasks_manager, "user_context": serialized_user}

        # return render(request, "personalarea/tasks.html", context=data_context)

        login = request.session.get('login')
        user = services.getUserWithLogin(login)
        serialized_user = {"login": login, "firstname": user.firstname, "lastname": user.lastname}
        data_context = {"user_context": serialized_user}
        return render(request, "personalarea/tasks.html", context=data_context)

def performers(request):
    if request.method == "POST":
        return HttpResponse("Ok")
    else:
        # login = request.session.get('login')
        # user = services.getUserWithLogin(login)

        # managers_persormers = {}
        # managers_persormers["performers"] = services.getAllUsersOfType("Performer")

        # managers_login = []
        # for performer in managers_persormers["performers"]:
        #     if performer.manager.login not in managers_login:
        #         managers_login.append(performer.manager.login)

        # queryset_manager = Manager.objects.filter(login__in=managers_login)
        # managers_persormers["managers"] = queryset_manager
        # serialized_managers_performers = ManagerForPerformerSerializer(managers_persormers).data

        # serialized_user = {"firstname": user.firstname, "lastname": user.lastname}

        # data_context = {"managers_performers_context": serialized_managers_performers, "user_context": serialized_user}
        # return render(request, "personalarea/performers.html", context=data_context)

        login = request.session.get('login')
        user = services.getUserWithLogin(login)
        serialized_user = {"firstname": user.firstname, "lastname": user.lastname}
        data_context = {"user_context": serialized_user}
        return render(request, "personalarea/performers.html", context=data_context)
