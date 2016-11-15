from django.conf.urls import patterns, include, url
from orders import views
from views import MakeOrder

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^pedir/$', MakeOrder.as_view(), name='order'),
	url(r'^contato/$', views.call, name='call'),
	url(r'^gerenciar/$', views.manage, name='manage'),
	url(r'^pedido/(?P<order_id>\d+)&', views.show, name='show'),
	url(r'^pedido_concluido/(?P<order_id>\d+)&', views.show_concluded, name='show_concluded'),
	url(r'^conclude/(?P<order_id>\d+)&', views.conclude, name='conclude'),
	url(r'^exclude/(?P<order_id>\d+)&', views.exclude, name='exclude')
)
