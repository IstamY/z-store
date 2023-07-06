from django.db import models
class Order(models.Model):
    # Define your Order model fields here
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
