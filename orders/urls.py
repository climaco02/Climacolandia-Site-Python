from django.conf.urls import patterns, include, url
from orders import views
from views import MakeOrder

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^pedir/$', MakeOrder.as_view(), name='order'),
	url(r'^contato/$', views.call, name='call')
)
