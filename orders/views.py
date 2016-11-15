from django.shortcuts import render, redirect
from django.views.generic.base import View
from orders.forms import MakeOrderForm
from orders.models import Order, OrdersConcluded

def index(request):
	return render(request, 'index.html')

def call(request):
	return render(request, 'call.html')

def manage(request):
	return render(request, 'manage.html', { 'orders' : Order.objects.all(), 'orders_concluded' : OrdersConcluded.objects.all() })

def conclude(request, order_id):
	order = Order.objects.get(id=order_id)
	order.conclude()
	return redirect('manage')

def show(request, order_id):
	order = Order.objects.get(id=order_id)
	already_concluded = order in OrdersConcluded.objects.all()
	return render(request, 'show.html', { 'order' : order , 'already_concluded' : already_concluded })

def show_concluded(request, order_id):
	order = OrdersConcluded.objects.get(id=order_id)
	already_concluded = order in OrdersConcluded.objects.all()
	return render(request, 'show.html', { 'order' : order , 'already_concluded' : already_concluded })


def exclude(request, order_id):
	order = Order.objects.get(id=order_id)
	order.exclude()
	return redirect('manage')

class MakeOrder(View):
	template_name = 'make_order.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = MakeOrderForm(request.POST)

		if form.is_valid():
			data_from_form = form.data

			order = Order(type_sweet=data_from_form['type_sweet'],
							description=data_from_form['description'])

			order.save()

			return redirect('call')

		return render(request, self.template_name, { 'form' : form })