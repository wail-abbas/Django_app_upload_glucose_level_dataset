from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import GlucoseLevel
from .serializers import GlucoseLevelSerializer
from .filters import GlucoseLevelFilter
from .pagination import DefaultPagination
from rest_framework.response import Response


class GlucoseLevelviewSet(ModelViewSet):
    """
    An API view to perform GET, POST, PUT, DELETE http actions to the GlucoseLevel model
    """
    queryset = GlucoseLevel.objects.all()
    serializer_class = GlucoseLevelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = GlucoseLevelFilter
    pagination_class = DefaultPagination
    search_fields = ['device__user_id__user_abbreviation', 'device_timestamp']
    ordering_fields = ['device__user_id__user_abbreviation', 'device_timestamp']
    ordering = ['device_timestamp']
    lookup_field = 'id'

    def get_serializer_context(self):
        return {'request': self.request}