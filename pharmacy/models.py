from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.user.username} - {self.medication.name}"
