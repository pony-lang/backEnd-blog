from rest_framework import serializers
from .models import DevTemplate, User


class DevTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevTemplate
        fields = (
            'id', 'title', 'description', 'img', 'device_type', 'is_custom_registered', 'protocal_type', 'updated',
            'created')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name', 'code', 'password', 'email', 'enabled'
        )
