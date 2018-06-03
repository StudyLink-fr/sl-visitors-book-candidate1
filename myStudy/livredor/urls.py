from django.conf.urls import url
from . import views

app_name = 'livredor'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'^ajout/$', views.create_message, name='create_message'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^(?P<pk>[0-9]+)/delete_message/$', views.delete_message, name='delete_message'),
]
