from django.db import models

class Order(models.Model):
	type_sweet = models.CharField(max_length=255, null=False)
	description = models.TextField(null=False)