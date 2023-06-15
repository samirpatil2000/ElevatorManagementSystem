from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from elevator.models import Elevator, Request
from elevator.serializers import ElevatorSerializer, RequestSerializer



class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer



