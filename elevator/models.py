from django.db import models

# Create your models here.


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
    current_floor = models.IntegerField(default=0)
    direction = models.CharField(
        max_length=20,
        choices=DIRECTION_CHOICES,
        default="Up")

    requests = models.ManyToManyField('elevator.Request', related_name='elevators')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Elevator {self.pk}"

    @classmethod
    def create_elevators(cls, n :int):
        for _ in range(n):
            cls.objects.create()


class Request(models.Model):
    floor = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Request to floor {self.floor}"

