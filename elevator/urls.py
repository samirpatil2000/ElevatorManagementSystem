
from django.urls import path, include
from rest_framework import routers

from .api_views import ElevatorViewSet, RequestViewSet, create_elevators

router = routers.DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('initialise-system/', create_elevators)
]