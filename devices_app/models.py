from django.db import models
from core_app.models import User

# Create your models here.
class Devices(models.Model):
    device_type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.device_type


class UserDevice(models.Model):
    serial_number = models.CharField(max_length=150, blank = False, unique = True)
    device_type = models.ForeignKey(Devices, on_delete=models.PROTECT, related_name='devices')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    
    def __str__(self) -> str:
        return self.serial_number
    