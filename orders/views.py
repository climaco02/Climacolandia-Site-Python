from django.shortcuts import render, redirect
from django.views.generic.base import View
from orders.forms import MakeOrderForm
from orders.models import Order

def index(request):
	return render(request, 'index.html')

def call(request):
	return render(request, 'call.html')

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