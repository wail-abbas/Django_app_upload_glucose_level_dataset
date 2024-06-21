from django.contrib import admin
from .models import Devices, UserDevice

# Register your models here.
admin.site.register(Devices)
admin.site.register(UserDevice)
