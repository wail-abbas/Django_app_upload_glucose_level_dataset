import django_filters
from django_filters.rest_framework import FilterSet
from .models import GlucoseLevel

class GlucoseLevelFilter(FilterSet):
  class Meta:
    model = GlucoseLevel
    fields = {
      'device_timestamp': ['gt', 'lt']
    }

