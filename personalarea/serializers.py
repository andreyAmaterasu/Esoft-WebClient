from rest_framework.serializers import ModelSerializer
from .models import Manager, Performer
from rest_framework import serializers

class ManagerSerializer(ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"

class PerformerSerializer(ModelSerializer):
    class Meta:
        model = Performer
        fields = "__all__"

class ManagerForPerformerSerializer(serializers.Serializer):
    managers = ManagerSerializer(read_only=True, many=True)
    performers = PerformerSerializer(read_only=True, many=True)