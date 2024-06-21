from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import GlucoseLevel
from .serializers import GlucoseLevelSerializer
from .filters import GlucoseLevelFilter
from .pagination import DefaultPagination

# Create your views here.
class GlucoseLevelviewSet(ModelViewSet):
    queryset = GlucoseLevel.objects.all()
    serializer_class = GlucoseLevelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_class = GlucoseLevelFilter
    search_fields = ['device', 'device_timestamp']
    ordering_fields = ['device', 'device_timestamp']
    ordering = ['device_timestamp']

    def get_queryset(self):
        queryset = super().get_queryset()
        device = self.request.query_params.get('device', None)
        if device:
            queryset = queryset.filter(device=device)


