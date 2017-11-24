from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),
	url(r'^(?P<post_id>\d+)/share/$', views.post_share, name = 'post_share'),
]