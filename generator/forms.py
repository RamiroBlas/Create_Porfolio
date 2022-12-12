from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(label=' Email', widget=forms.EmailInput())
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k: "" for k in fields}


class PerfilForm(forms.ModelForm):
	url_imagen = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'url imagen'}), required=True)
	titulo = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'título del proyecto'}), required=True)
	descripcion = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'descripción del proyecto'}), required=True)

	class Meta:
		model = Perfil
		fields = ['url_imagen','titulo','descripcion']