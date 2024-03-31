from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from pharmacy.forms import FakeOrderForm
from pharmacy.models import FakeOrder, Medication


# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Medication.objects.all()[3:]
        context = {"products": products}
        return render(request, 'pharmacy/index.html', context)


class StoreView(View):
    def get(self, request):
        products = Medication.objects.all()
        paginator = Paginator(products, 9)

        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context = {
            "products": products,
            "page_object": page_object
        }
        return render(request, 'pharmacy/store.html', context)


class StoreItemView(View):
    def get(self, request, slug, *args, **kwargs):
        product = Medication.objects.get(slug=slug)
        form = FakeOrderForm(initial={'medication': product})
        context = {'product': product, 'form': form}
        return render(request, 'pharmacy/store-item.html', context)

    def post(self, request, slug, *args, **kwargs):
        form = FakeOrderForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Medication, slug=slug)
            fake_order = form.save(commit=False)
            fake_order.medication = product
            fake_order.save()
            # medication.stock_quantity -= fake_order.quantity
            product.save()
            return redirect(reverse('confirmation'))  # Redirect to success page or any other page
        else:
            product = get_object_or_404(Medication, slug=slug)
            context = {'product': product, 'form': form}
            return render(request, 'pharmacy/store-item.html', context)


class CheckoutView(View):
    pass


class ConfirmationView(View):
    def get(self, request):
        orders = FakeOrder.objects.all()
        return render(request, 'pharmacy/confirmation.html', {"orders": orders})


class AboutView(View):
    pass
