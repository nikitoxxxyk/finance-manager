from django.contrib import admin
from django.urls import include, path
from main import views as views_main
from menu import views as views_menu

app_name = 'menu'

urlpatterns = [
	path('', views_menu.menu, name='menu'),
	path('transactions/', views_menu.transaction_list, name='transaction_list'),
	path('transactions/add/', views_menu.transaction_add, name='transaction_add'),
	path('categories', views_menu.category_list, name='category_list')
]
