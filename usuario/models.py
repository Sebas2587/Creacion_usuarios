from __future__ import unicode_literals

from distutils.command.upload import upload

from django.conf import settings
from django.db import models


#se utilizara modelo creado por django para la creacion de usuarios y perfiles

class Usuario_perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    photo = models.ImageField(upload_to='perfil', blank=True, null=True)
    ubicacion = models.CharField(max_length=255, null=True)
    descripcionUser = models.TextField(null=True)



