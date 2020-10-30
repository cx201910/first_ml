from django.conf.urls import re_path, include
from rest_framework.routers import DefaultRouter

from .views import EndpointViewSet
from .views import MLAlgorithmViewSet
from .views import MLAlgorithmStatusViewSet
from .views import MLRequestViewSet
from apps.endpoints.views import PredictView
from apps.endpoints.views import ABTestViewSet
from apps.endpoints.views import StopABTestView
from apps.endpoints.views import PredictStoreViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'endpoints', EndpointViewSet, basename='endpoints')
router.register(r'mlalgorithms', MLAlgorithmViewSet, basename='mlalgorithms')
router.register(r"predictstore", PredictStoreViewSet, basename="predictstore")
router.register(r'mlalgorithmstatuses', MLAlgorithmStatusViewSet, basename='mlalgorithmstatuses')
router.register(r'mlrequests', MLRequestViewSet, basename='mlrequests')
router.register(r'abtests', ABTestViewSet, basename='abtests')
urlpatterns = [
    re_path(r'^api/v1/', include(router.urls)),
    re_path(r'^api/v1/(?P<endpoint_name>.+)/predict$', PredictView.as_view(), name='predict'),
    re_path(r'^api/v1/stop_ab_test/(?P<ab_test_id>.+)', StopABTestView.as_view(), name='stop_ab'),
]
