from django.db import models

class Order(models.Model):
	type_sweet = models.CharField(max_length=255, null=False)
	description = models.TextField(null=False)

	def conclude(self):
		order_concluded = OrdersConcluded(type_sweet=self.type_sweet, 
			description=self.description)
		order_concluded.save()
		self.delete()

	def exclude(self):
		self.delete()

class OrdersConcluded(models.Model):
	type_sweet = models.CharField(max_length=255, null=False)
	description = models.TextField(null=False)