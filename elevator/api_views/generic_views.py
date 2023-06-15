from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, status
from rest_framework.response import Response

from elevator.models import Elevator, Request
from elevator.serializers import ElevatorSerializer, RequestSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data={**request.data, 'is_completed': True}
        )

        try:

            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            floor = serializer.data.get("floor")
            elevator = Elevator.get_nearest_elevator(floor)
            elevator.is_door_opened = True
            elevator.save()
            elevator.requests.add(serializer.instance.id)

            return Response(
                data={"message": f"Requested for elevator successfully Elevator {elevator.pk} is on the way"},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                data={"message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
