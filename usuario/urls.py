from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from usuario.views import registro_usuario_view, perfil

urlpatterns = [
    url(r'^$', registro_usuario_view, name='usuario.registro_usuario_view'),
    url(r'^registro$', registro_usuario_view, name='usuario.registro_usuario_view'),
    url(r'^gracias$', perfil, name='usuario.perfil'),
    # (?P<username>[\w]+) que es una simple expresion regular, donde
    # <username> es la variable que pasara a la vista con el valor [\w]+
    #url(r'perfil$', gracias_view, name='gracias'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
