from django.contrib import admin

from pharmacy.models import Medication, Customer, Order


# Register your models here.
@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "stock_quantity")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "phone_number")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "medication", "quantity", "order_date", "is_confirmed")
