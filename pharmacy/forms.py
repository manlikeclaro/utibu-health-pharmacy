from django import forms
from django.core.exceptions import ValidationError

from pharmacy.models import FakeOrder


class FakeOrderForm(forms.ModelForm):
    class Meta:
        model = FakeOrder
        fields = ['medication', 'quantity']

    def __init__(self, *args, **kwargs):
        super(FakeOrderForm, self).__init__(*args, **kwargs)
        self.fields['medication'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control text-center',
            'placeholder': 'Enter quantity',
            'aria-label': 'Example text with button addon',
            'aria-describedby': 'button-addon1',
            'min': '1'
        })

        # Set initial max value for quantity (this will be updated dynamically)
        # self.fields['quantity'].widget.attrs['max'] = '20'

        # Add JavaScript class to quantity field for easier targeting
        self.fields['quantity'].widget.attrs['class'] += ' dynamic-max'

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        medication = self.cleaned_data.get('medication')
        if medication and quantity > medication.stock_quantity:
            raise ValidationError("Quantity can't be more than available stock")
        return quantity
