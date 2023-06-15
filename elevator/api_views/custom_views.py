import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elevator.models import Elevator
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_elevators(request):
    payload = request.data
    elevators = payload.get("elevators")
    if not elevators or not elevators.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Elevators in response should be numeric"})
    try:

        Elevator.create_elevators(n=int(elevators))
        return Response({"message": "Elevators Created Successfully"})

    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": str(e)})


@api_view(['POST'])
def destination_request(request, elevator_id: int):
    payload = request.data
    floor = payload.get("floor")
    if not floor or not floor.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Floor in response should be numeric"})

    elevator = get_object_or_404(Elevator, id=elevator_id)

    try:

        elevator.current_floor = payload.get('floor')
        elevator.is_door_opened = False
        elevator.save()

        return Response({"message": f"Elevator {elevator.pk} Reach To destination floor {floor}"})

    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": str(e)})
