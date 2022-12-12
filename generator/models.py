from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return f'Perfil de {self.user.username}'

	
class Perfil(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
	timestamp = models.DateTimeField(default=timezone.now)
	url_imagen= models.TextField()
	titulo = models.TextField()
	descripcion= models.TextField()
    

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: { self.url_imagen, self.titulo, self.descripcion}'