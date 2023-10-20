# Create your views here.
from drf_yasg import views
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import DevTemplate, User
from demo.serializers import DevTemplateSerializer, UserSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from rest_framework_simplejwt import authentication

from .utils.Authentications import MyJWTAuthentication


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


class TestView(views.APIView):
    # permission_classes = [permissions.AllowAny]
    # authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]

    def get(self, request, *args, **kwargs):
        # print('authenticate: ', request.successful_authenticator.authenticate(request))
        # print('authenticate_header: ', request.successful_authenticator.authenticate_header(request))
        # print('get_header: ', request.successful_authenticator.get_header(request))
        # print('get_raw_token: ',
        #       request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request)))
        # print('get_validated_token: ', request.successful_authenticator.get_validated_token(
        #     request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request))))
        # print('get_user: ', request.successful_authenticator.get_user(
        #     request.successful_authenticator.get_validated_token(
        #         request.successful_authenticator.get_raw_token(request.successful_authenticator.get_header(request)))))
        # print('www_authenticate_realm: ', request.successful_authenticator.www_authenticate_realm)
        return Response('OK')

    def post(self, request, *args, **kwargs):
        return Response('OK')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [MyJWTAuthentication, SessionAuthentication, BasicAuthentication]
