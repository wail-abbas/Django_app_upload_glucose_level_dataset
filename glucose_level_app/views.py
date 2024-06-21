from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import GlucoseLevel
from .serializers import GlucoseLevelSerializer
from .filters import GlucoseLevelFilter
from .pagination import DefaultPagination
from rest_framework.response import Response

# Create your views here.
class GlucoseLevelviewSet(ModelViewSet):
    
    serializer_class = GlucoseLevelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_class = GlucoseLevelFilter
    search_fields = ['device', 'device_timestamp']
    ordering_fields = ['device', 'device_timestamp']
    ordering = ['device_timestamp']
    lookup_field = 'id'

    def get_queryset(self):
        queryset = GlucoseLevel.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        
        if user_id:
            queryset = queryset.filter(device__user_id__user_abbreviation=user_id).select_related('device')
        
        return queryset
