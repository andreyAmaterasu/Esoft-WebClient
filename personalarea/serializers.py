from rest_framework.serializers import ModelSerializer
from .models import Manager, Performer, Task, Useraccount
from rest_framework import serializers



class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = ('login', 'firstname', 'lastname', 'patronymic')

class PerformerSerializer(ModelSerializer):
    manager = ManagerSerializer()

    class Meta:
        model = Performer
        fields = ('login', 'firstname', 'lastname', 'patronymic', 'grade', 'manager',)

class TaskPerformerManagerSerializer(ModelSerializer):
    taskperformer = PerformerSerializer()

    class Meta:
        model = Task
        fields = ('taskid', 'taskname', 'aboutoftask', 'periodofexecution', 'dateofcompletion', 'taskcomplexity', 'timetocompletethetask', 'taskstatus', 'natureofthetask', 'taskperformer')

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    