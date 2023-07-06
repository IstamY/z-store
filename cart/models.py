from django.db import models
from products.models import Product

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Add other fields if necessary

    def subtotal(self):
        return self.product.price * self.quantity

class Order(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    payment_method = models.CharField(max_length=50)
    # Add other fields as needed

    def __str__(self):
        return f"Order #{self.id}"