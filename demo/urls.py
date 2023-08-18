from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from . import views
from .views import DevTemplateViewSet
router = routers.DefaultRouter()
router.register(r'demo', DevTemplateViewSet, basename='demo')

urlpatterns = [
    url(r'^', include(router.urls)),
]
