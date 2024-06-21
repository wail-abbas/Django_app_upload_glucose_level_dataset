from rest_framework import serializers
from core_app.models import User
from .models import Devices, UserDevice

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "user_abbreviation"]

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = ["device_type"]

class UserDeviceSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    device_type = DeviceSerializer()
    class Meta:
        model = UserDevice
        fields = ["serial_number", "device_type", "user_id"]