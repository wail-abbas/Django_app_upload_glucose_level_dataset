from rest_framework_nested import routers
from .views import GlucoseLevelviewSet

router = routers.DefaultRouter()
router.register('levels', GlucoseLevelviewSet, basename='levels')

urlpatterns = router.urls 