from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PerfilForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

def index(request):
    return render(request, 'index.html')

class feed(ListView):
	model= Perfil
	template_name= 'feed.html'
	context_object_name = 'projects'

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('index')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'register.html', context)

@login_required
def create_project(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PerfilForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Proyecto creado')
			return redirect('feed')
	else:
		form = PerfilForm()
	return render(request, 'project.html', {'form' : form })

#profile
def profile(request, username=None):
	current_user = request.user
	print(username)
	print(current_user.username)
	contexto={}
	if username and username == current_user.username:
		contexto['user'] = User.objects.get(username=username)
		contexto['project'] = Project.objects.all()
	else: 
		user = current_user
	return render(request, 'profile.html', context=contexto)



@login_required
def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("feed")
