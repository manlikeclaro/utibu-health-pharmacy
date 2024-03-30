from django import forms

from pharmacy.models import FakeOrder


class FakeOrderModelForm(forms.ModelForm):
    class Meta:
        model = FakeOrder
        # fields = ('',)
        exclude = ('order_date', 'total_price')
