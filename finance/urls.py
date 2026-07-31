from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
# from main import views 
# from menu import views

urlpatterns = [
	path('', include('main.urls', namespace='main')),
	path('menu/', include('menu.urls', namespace='menu')),
	path('admin/', admin.site.urls),
	# re_path(r'^about/contact', views.contact, name='about'),
	# re_path(r'^about', views.about, name='about'),
]
