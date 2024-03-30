from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Medication(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    stock_quantity = models.IntegerField(default=0)
    slug = models.SlugField(default="", null=False, unique=True)

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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None)

    def save(self, *args, **kwargs):
        self.price = self.medication.price * self.quantity
        if self.medication.stock_quantity >= self.quantity:
            self.medication.stock_quantity -= self.quantity
        super().save()

    def __str__(self):
        return f"{self.customer.user.username} - {self.medication.name}"


class FakeOrder(models.Model):
    medication = models.CharField(max_length=100)
    medication_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=None, editable=False)

    def save(self, *args, **kwargs):
        self.total_price = self.medication_price * self.quantity
        super().save()

    def __str__(self):
        return f"{self.medication}"
