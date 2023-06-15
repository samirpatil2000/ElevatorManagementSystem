from django.db import models

# Create your models here.
from django.db.models import Func, F


class Elevator(models.Model):
    OPERATIONAL = 'operational'
    MAINTENANCE = 'maintenance'
    STATUS_CHOICES = [
        (OPERATIONAL, 'Operational'),
        (MAINTENANCE, 'Maintenance'),
    ]

    DIRECTION_CHOICES = [
        ("UP", 'Up'),
        ("DOWN", 'Down'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=OPERATIONAL
    )
    current_floor = models.IntegerField(default=0, db_index=True)
    direction = models.CharField(
        max_length=20,
        choices=DIRECTION_CHOICES,
        default="Up")

    requests = models.ManyToManyField('elevator.Request', related_name='elevators', blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    is_door_opened = models.BooleanField(default=False)

    def __str__(self):
        return f"Elevator {self.pk} Current Floor {self.current_floor}"

    @classmethod
    def create_elevators(cls, n :int):
        for _ in range(n):
            cls.objects.create()

    @classmethod
    def get_nearest_elevator(cls, floor: int):
        return cls.objects.annotate(diff=Func(F('current_floor') - floor, function='ABS')).order_by('diff').first()


class Request(models.Model):
    floor = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Request to floor {self.floor}"

