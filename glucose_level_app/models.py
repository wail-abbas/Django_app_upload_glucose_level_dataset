from django.db import models
from django.core.validators import MaxLengthValidator
from devices_app.models import UserDevice
# Create your models here.

class GlucoseLevel(models.Model):
    RECORD_TYPE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('2', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]

    device = models.ForeignKey(UserDevice, on_delete=models.PROTECT, related_name='user_devices')
    device_timestamp = models.DateTimeField(blank = False)
    record_type = models.CharField(max_length=1, choices=RECORD_TYPE_CHOICES)
    glucose_history_mg_dL = models.FloatField(blank = True, null = True)
    glucose_scan_mg_dL = models.FloatField(blank = True, null = True)
    non_numeric_rapid_acting_insulin  = models.FloatField(blank = True, null = True)
    rapid_acting_insulin_units = models.FloatField(blank = True, null = True)
    non_numeric_food_data = models.FloatField(blank = True, null = True)
    carbohydrates_grams = models.FloatField(blank = True, null = True)
    carbohydrates_servings = models.FloatField(blank = True, null = True)
    non_numeric_depot_insulin = models.FloatField(blank = True, null = True)
    depot_insulin_units = models.FloatField(blank = True, null = True)
    notes = models.TextField(max_length=250, blank=True, validators=[MaxLengthValidator(250)])
    glucose_test_strip_mg_dL = models.FloatField(blank = True, null = True)
    ketone_mmol_L = models.FloatField(blank = True, null = True)
    mealtime_insulin_units = models.FloatField(blank = True, null = True)
    correction_insulin_units = models.FloatField(blank = True, null = True)
    user_insulin_change_units = models.FloatField(blank = True, null = True)

    def __str__(self) -> str:
        return self.device_timestamp.strftime('%Y-%m-%d %H:%M:%S')
