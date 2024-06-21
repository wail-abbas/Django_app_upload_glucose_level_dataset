from rest_framework_nested import routers
from .views import GlucoseLevelviewSet

router = routers.DefaultRouter()
router.register('levels', GlucoseLevelviewSet, basename='levels')
router.register('levels/<int:id>/', GlucoseLevelviewSet, basename='levels_row')

urlpatterns = router.urls 