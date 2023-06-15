from rest_framework import serializers
from .models import Elevator, Request


class RequestSerializer(serializers.ModelSerializer):
    is_completed = serializers.BooleanField(read_only=True)
    class Meta:
        model = Request
        fields = ('floor', 'timestamp', 'is_completed')


class ElevatorSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True, read_only=True)

    class Meta:
        model = Elevator
        fields = '__all__'