from rest_framework.serializers import ModelSerializer
from .models import Manager, Performer, Task
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

class TaskSerializer(ModelSerializer):
    taskperformer = PerformerSerializer()

    class Meta:
        model = Task
        fields = ('taskid', 'taskname', 'aboutoftask', 'periodofexecution', 'dateofcompletion', 'taskcomplexity', 'timetocompletethetask', 'taskstatus', 'natureofthetask', 'taskperformer')

class ManagerForPerformerSerializer(serializers.Serializer):
    managers = ManagerSerializer(many=True)
    performers = PerformerSerializer(many=True)

class TasksPerformerManagerSerializer(serializers.Serializer):
    tasks = TaskSerializer(read_only=True, many=True)
    performers = PerformerSerializer(read_only=True)
    manager = ManagerSerializer(read_only=True)

class TasksManagerPerformersSerializer(serializers.Serializer):
    tasks = TaskSerializer(read_only=True, many=True)
    manager = ManagerSerializer(read_only=True)
    performers = PerformerSerializer(read_only=True, many=True)
    