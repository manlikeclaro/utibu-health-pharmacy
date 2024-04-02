from django.contrib import admin

from pharmacy.models import Medication, Customer, Order


# Register your models here.
@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description", "stock_quantity")
    readonly_fields = ("slug", "short_description")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "phone_number")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "medication", "quantity", "order_date", "total_price")
    readonly_fields = ("total_price",)


# @admin.register(FakeOrder)
# class FakeOrderAdmin(admin.ModelAdmin):
#     list_display = ("medication", "quantity", "order_date", "total_price")
#     # readonly_fields = ("medication.price",)
