from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from pharmacy.models import FakeOrder


class FakeOrderModelForm(forms.ModelForm):
    class Meta:
        model = FakeOrder
        # fields = ('',)
        exclude = ('order_date', 'total_price')

    def __init__(self, *args, **kwargs):
        product = kwargs.pop('product', None)  # Get the product object passed as argument
        super().__init__(*args, **kwargs)

        self.fields['quantity'].widget.attrs.update(
            {'class': 'form-control text-center', 'placeholder': 'Enter quantity',
             'aria-label': 'Example text with button addon', 'aria-describedby': 'button-addon1'})
        self.fields['quantity'].widget.input_type = 'text'

        # self.fields['quantity'].validators.extend([
        #     MinValueValidator(1),
        #     MaxValueValidator(self.instance.product.stock_quantity)  # Set maximum value to product stock quantity
        # ])

        # Set initial values for form fields from the product object
        if product:
            self.initial['medication'] = product.name
            self.initial['medication_price'] = product.price

    def clean_quantity(self):
        # Ensure quantity is a positive integer
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be a positive integer.")
        return quantity
