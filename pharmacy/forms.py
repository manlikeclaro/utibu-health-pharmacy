from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from pharmacy.models import Order, Customer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['medication', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
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


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'username'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'password'
        })

        # Add labels to form fields
        self.fields['username'].label = 'Enter Username'
        self.fields['password'].label = 'Enter Password'


class CustomUserCreationForm(UserCreationForm):
    # address = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'id': 'username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'password1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'password2'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'id': 'phone_number'
        })

        # Add labels to form fields
        self.fields['username'].label = 'Enter Username'
        self.fields['password1'].label = 'Enter Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['phone_number'].label = 'Enter Phone Number'
