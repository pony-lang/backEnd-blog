"""frontBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.models import User
from rest_framework import serializers, routers, viewsets
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^devtemplate/', include('demo.urls')),
    url(r'^token-api/token/$codeholder_1amp;#39;', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    url(r'^token-api/token/refresh/$codeholder_1amp;#39;', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^token-api/token/verify/$codeholder_1amp;#39;', TokenVerifyView.as_view(), name='token_verify'),
]
