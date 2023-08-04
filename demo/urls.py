from django.conf.urls import include, url
from rest_framework import routers
from .views import DevTemplateViewSet

router = routers.DefaultRouter()
router.register(r'demo', DevTemplateViewSet, basename='demo')

urlpatterns = [
    url(r'^', include(router.urls))
]
