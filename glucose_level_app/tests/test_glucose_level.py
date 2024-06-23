
from rest_framework import status
import pytest
from model_bakery import baker
from glucose_level_app.models import GlucoseLevel


@pytest.mark.django_db
class TestGlucoseLevelEndpoit:
    """
    This test will create a dummy using model_bakery data and retrieve it by its id
    """

    def test_glucose_level_get_returns_200(self, api_client):
        glucose_level = baker.make(GlucoseLevel)

        response = api_client.get(f'/api/v1/levels/{glucose_level.id}/')

        assert response.status_code == status.HTTP_200_OK