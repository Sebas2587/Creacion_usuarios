from django.contrib import admin
from .models import Usuario_perfil


@admin.register(Usuario_perfil)
class usuarioPadmin(admin.ModelAdmin):

    list_filter = ('descripcionUser',)

