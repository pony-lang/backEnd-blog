from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.
import uuid
from django.utils.translation import ugettext_lazy as _


class DevTemplate(models.Model):
    """
		設備模板表
	"""
    MQTT = 'MQTT'
    HTTP = 'HTTP'
    CoAP = 'CoAP'
    PROTOCOL_CHOICES = (
        (MQTT, 'MQTT'),
        (HTTP, 'HTTP'),
        (CoAP, 'CoAP'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=80, blank=True)
    description = models.TextField(_(u"Description"), blank=True)
    img = models.ImageField(upload_to='image', default='upload/none.png', blank=True)
    device_type = models.CharField(max_length=40, blank=True)
    is_custom_registered = models.BooleanField(default=False)
    protocal_type = models.CharField(max_length=200, choices=PROTOCOL_CHOICES, default=HTTP)
    updated = models.DateTimeField(_(u"Update date"), auto_now=True)
    created = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    code = models.CharField(max_length=64, unique=True, verbose_name='用户编码')
    name = models.CharField(max_length=128, verbose_name='用户中文名')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    enabled = models.IntegerField(default=1, verbose_name='是否启用', choices=((1, '启用'), (0, '停用')))

    @property
    def is_authenticated(self):
        """
		Always return True. This is a way to tell if the user has been
		authenticated in templates.
		"""
        return True
