# Create your views here.

from .models import DevTemplate, User
from demo.serializers import DevTemplateSerializer, UserSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.authentication import BasicAuthentication

from rest_framework_simplejwt import authentication


class DevTemplateViewSet(viewsets.ModelViewSet):
    """
    list:
    查询设备模板列表

    create：
    创建设备模板

    retrieve:
    查询设备模板详情
    """

    serializer_class = DevTemplateSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    queryset = DevTemplate.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = DevTemplate.objects.filter(owner=request.user).order_by('-created')
        # queryset = DevTemplate.objects.all()

        self.check_object_permissions(request, DevTemplate)
        serializer = DevTemplateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # queryset = DevTemplate.objects.filter(owner=request.user)
        queryset = DevTemplate.objects.all()
        queryset_tmp = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(request, DevTemplate)
        serializer = DevTemplateSerializer(queryset_tmp)
        return Response(serializer.data)


class TestView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *agrs, **kwargs):
        return Response('OK')

    def post(self, request, *args, **kwargs):
        return Response('OK')
