from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^livredor/', include('livredor.urls')),
	url(r'^admin/', admin.site.urls),
]
