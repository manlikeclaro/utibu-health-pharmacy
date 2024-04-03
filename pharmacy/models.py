import secrets
import string

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


def generate_transaction_id(order_id):
    alphabet = string.ascii_letters + string.digits
    transaction_id = ''.join(secrets.choice(alphabet) for i in range(6))  # Adjust the length as needed
    return f"{order_id}-{transaction_id}"


# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    medication_image = models.ImageField(upload_to='pharmacy/images', default='pharmacy/images/default_image.png')
    description = models.TextField()
    short_description = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    stock_quantity = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    sale = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.short_description = self.description[:100]
        super().save()

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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    medication = models.ForeignKey(Medication, on_delete=models.SET_NULL, null=True)
    medication_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None, editable=False)
    transaction_id = models.CharField(max_length=20, unique=True, editable=False, default='')

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = generate_transaction_id(self.customer.id)

        self.medication_price = self.medication.price
        self.total_price = self.medication_price * self.quantity

        # Check if there's enough quantity in stock to fulfill the order
        if self.medication.stock_quantity >= self.quantity:
            self.medication.stock_quantity -= self.quantity
            self.medication.save()  # Update medication stock quantity
            super().save()  # Save only if there's enough quantity in stock
        else:
            # If there's not enough quantity in stock, you may raise an exception,
            # log a message, or handle the situation as per your application's requirements.
            raise ValueError("Not enough quantity in stock to fulfill the order")

    def __str__(self):
        if self.customer and self.customer.user.first_name:  # Check if customer and user exist
            return f"{self.medication} - {self.customer.user.first_name}"
        else:
            return f"{self.medication} - Unknown Customer"  # Provide fallback if customer or user doesn't exist

# class FakeOrder(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
#     medication = models.ForeignKey(Medication, on_delete=models.SET_NULL, null=True)
#     medication_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
#     quantity = models.IntegerField(default=1)
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None, editable=False)
#     transaction_id = models.CharField(max_length=20, unique=True, editable=False, default='')
#
#     def save(self, *args, **kwargs):
#         if not self.transaction_id:
#             self.transaction_id = generate_transaction_id(self.customer.id)
#
#         self.medication_price = self.medication.price
#         self.total_price = self.medication_price * self.quantity
#
#         # Check if there's enough quantity in stock to fulfill the order
#         if self.medication.stock_quantity >= self.quantity:
#             self.medication.stock_quantity -= self.quantity
#             self.medication.save()  # Update medication stock quantity
#             super().save()  # Save only if there's enough quantity in stock
#         else:
#             # If there's not enough quantity in stock, you may raise an exception,
#             # log a message, or handle the situation as per your application's requirements.
#             raise ValueError("Not enough quantity in stock to fulfill the order")
#
#     # def __str__(self):
#     #     return f"{self.medication} - {self.customer.user.first_name}"
#
#     def __str__(self):
#         if self.customer and self.customer.user.first_name:  # Check if customer and user exist
#             return f"{self.medication} - {self.customer.user.first_name}"
#         else:
#             return f"{self.medication} - Unknown Customer"  # Provide fallback if customer or user doesn't exist
