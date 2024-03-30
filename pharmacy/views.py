from django.shortcuts import render, redirect
from django.views import View

from pharmacy.forms import FakeOrderModelForm
from pharmacy.models import FakeOrder


# Create your views here.
class HomeView(View):
    def get(self, request):
        form = FakeOrderModelForm()
        return render(request, 'pharmacy/index.html', {"form": form})

    def post(self, request):
        form = FakeOrderModelForm(request.POST)
        form.save()
        return redirect('confirmation')


class StoreView(View):
    pass


class StoreItemView(View):
    pass


class CheckoutView(View):
    pass


class ConfirmationView(View):
    def get(self, request):
        orders = FakeOrder.objects.all()
        return render(request, 'pharmacy/confirmation.html', {"orders": orders})


class AboutView(View):
    pass
