from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('Rider', 'Rider'),
        ('Driver', 'Driver'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
class Trip(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    rider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rider_trips')
    driver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='driver_trips')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rider.username} - {self.pickup_location} to {self.dropoff_location}"
