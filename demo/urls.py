from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from . import views
from .utils.Authentications import MyTokenObtainPairView
router = routers.DefaultRouter()
router.register(r'demo', views.DevTemplateViewSet, basename='demo')

urlpatterns = [
    url(r'^', include(router.urls)),
    # jwt
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('test/', views.TestView.as_view(), name='test'),
    # jwt
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
