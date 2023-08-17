from django.conf.urls import include, url
from rest_framework import routers
from .views import DevTemplateViewSet, TestView


router = routers.DefaultRouter()
router.register(r'demo', DevTemplateViewSet, basename='demo')
router.register(r'test', TestView, basename='test')

urlpatterns = [
    url(r'^', include(router.urls))
]
