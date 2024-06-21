from rest_framework import serializers
from .models import GlucoseLevel
from devices_app.serializers import UserDeviceSerializer

class GlucoseLevelSerializer(serializers.ModelSerializer):
    device = UserDeviceSerializer()

    class Meta:
        model = GlucoseLevel
        fields = [  
                    "device",
                    "device_timestamp", 
                    "record_type", 
                    "glucose_history_mg_dL", 
                    "glucose_scan_mg_dL", 
                    "non_numeric_rapid_acting_insulin", 
                    "rapid_acting_insulin_units", 
                    "non_numeric_food_data", 
                    "carbohydrates_grams", 
                    "carbohydrates_servings", 
                    "non_numeric_depot_insulin", 
                    "depot_insulin_units", 
                    "notes", 
                    "glucose_test_strip_mg_dL", 
                    "ketone_mmol_L", 
                    "mealtime_insulin_units", 
                    "correction_insulin_units", 
                    "user_insulin_change_units",
                    ]
        
