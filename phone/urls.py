from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.recordList, name='recordList'),
	url(r'^record/(?P<pk>[0-9]+)/$', views.recordDetail, name='recordDetail'),
	url(r'^record/new/$', views.recordNew, name='recordNew'),
	url(r'^record/(?P<pk>[0-9]+)/edit/$', views.recordEdit, name='recordEdit'),
	url(r'^record/(?P<pk>[0-9]+)/delete/$', views.recordDelete, name='recordDelete'),
	url(r'^record/search/$', views.recordSearch, name='recordSearch'),
]