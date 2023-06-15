import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elevator.models import Elevator


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