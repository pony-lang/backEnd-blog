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
from rest_framework import serializers, routers, viewsets, permissions
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from demo.utils.Authentications import MyTokenObtainPairView
from demo.views import TestView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="博客接口文档平台",
        default_version='v1',
        description="博客文档描述v1",
        terms_of_service="",
        contact=openapi.Contact(email="mhcode@qq.com"),
        license=openapi.License(name="BSD LICENSE"),
        public=True,
        permission_classes=(permissions.AllowAny,)
    ),
    public=True
)


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

    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    url(r"^docs/", include_docs_urls(title="My API Titile")),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),

    path('login/', MyTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('verify/', TokenVerifyView.as_view(), name="token_verify"),
    path("test/", TestView.as_view(), name="token_refresh"),
]
