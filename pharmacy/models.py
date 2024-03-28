from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    stock_quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Medication"

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
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None)

    def save(self, *args, **kwargs):
        self.price = self.medication.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.user.username} - {self.medication.name}"
