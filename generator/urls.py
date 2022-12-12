from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from generator.views import feed,profile,register,create_project,index, deleteProject
 
urlpatterns = [
	path('', index, name='index'),
	path('feed/', feed.as_view(), name='feed'),
	path('profile/', profile, name='profile'),
	path('profile/<str:username>/', profile, name='profile'),
	path('register/', register, name='register'),
	path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
	path('proyecto/', create_project, name='proyecto'),
	path('delete/<int:id>', deleteProject, name="delete"),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

