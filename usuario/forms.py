# coding=utf-8
from django import forms
from django.contrib.auth.models import User


class RegistroUser(forms.Form):
    username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField()
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password2'}))

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya esta registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db.')
        return email

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password


class LlenadoPerfil(forms.Form):
    photo = forms.ImageField()
    ubicacion = forms.CharField()
    descripcionUser = forms.Textarea()

