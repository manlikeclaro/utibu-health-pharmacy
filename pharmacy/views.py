from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from pharmacy.forms import FakeOrderModelForm
from pharmacy.models import FakeOrder, Medication


# Create your views here.
class HomeView(View):
    def get(self, request):
        form = FakeOrderModelForm()
        products = Medication.objects.all()[3:]
        response_data = {
            "products": products,
            "form": form
        }
        return render(request, 'pharmacy/index.html', context=response_data)

    def post(self, request):
        form = FakeOrderModelForm(request.POST)
        form.save()
        return redirect('confirmation')


class StoreView(View):
    def get(self, request):
        products = Medication.objects.all()
        paginator = Paginator(products, 9)

        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)

        response_data = {
            "products": products,
            "page_object": page_object
        }
        return render(request, 'pharmacy/store.html', context=response_data)


class StoreItemView(View):
    def get(self, request, slug):
        product = get_object_or_404(Medication, slug=slug)
        form = FakeOrderModelForm(initial={'medication': product.name, 'medication_price': product.price})
        # Pass initial values for medication and medication_price here

        response_data = {
            "product": product,
            "form": form
        }

        return render(request, 'pharmacy/store-item.html', context=response_data)

    def post(self, request, slug):  # Add the 'slug' parameter here
        product = get_object_or_404(Medication, slug=slug)
        form = FakeOrderModelForm(request.POST)
        if form.is_valid():
            fake_order = form.save(commit=False)
            fake_order.medication = product.name  # Assign product name to medication field
            fake_order.medication_price = product.price  # Assign product price to medication_price field
            fake_order.save()
            return redirect('confirmation')


class CheckoutView(View):
    pass


class ConfirmationView(View):
    def get(self, request):
        orders = FakeOrder.objects.all()
        return render(request, 'pharmacy/confirmation.html', {"orders": orders})


class AboutView(View):
    pass
