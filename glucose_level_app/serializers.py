from rest_framework import serializers
from .models import GlucoseLevel
from devices_app.serializers import UserDeviceSerializer

class GlucoseLevelSerializer(serializers.ModelSerializer):
    device = UserDeviceSerializer()

    class Meta:
        model = GlucoseLevel
        fields = '__all__'
