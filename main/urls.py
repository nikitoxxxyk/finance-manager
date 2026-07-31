from django.contrib import admin
from django.urls import include, path
from main import views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),

	# namespace = 'main'
	path('register/', views.register_view, name='register'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),


	# Для авторизованных пользователей
	# path('main/menu/', include('menu.urls', namespace='menu'), name='menu'),
	# path('menu/add_transaction/', views.)
]
