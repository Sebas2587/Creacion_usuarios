from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from usuario.models import Usuario_perfil
from .forms import RegistroUser, LlenadoPerfil


def registro_usuario_view(request):
    if request.method == 'POST':
        form = RegistroUser(request.POST, request.FILES)
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor, donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            user_model = User.objects.create_user(username=username, password=password)
            # Anadimos el email
            user_model.email = email
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = Usuario_perfil()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo (el campo, permite datos null)
            # user_profile.photo = photo
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
            # Ahora, redireccionamos a la pagina accounts/gracias.html
            # Pero lo hacemos con un redirect.

            return render(request, 'accounts/gracias.html', {'username': username},
                          context_instance=RequestContext(request))

    else:
        form = Usuario_perfil()
    context = {
        'form': form
    }
    return render(request, "accounts/registro.html", context)


def perfil(request):
    if request.method == 'POST':
        form = LlenadoPerfil(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            photo = cleaned_data.get('photo')
            ubicacion = cleaned_data.get('ubicacion')
            descripcionUser = cleaned_data.get('descripcionUser')
            perfil_user = User.objects.create_user(photo=photo, ubicacion=ubicacion, descripcionUser=descripcionUser)
            perfil_user.save()
            user_perfil = Usuario_perfil()
            user_perfil.user = perfil_user
            user_perfil.save()
            return render(request, 'accounts/gracias.html', {'username': User.username},
                          context_instance=RequestContext(request))
        else:
            form = LlenadoPerfil()
        context = {
            'form': form
        }
        return render(request, "accounts/gracias.html", context)



