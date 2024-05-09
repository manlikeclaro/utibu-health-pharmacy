import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pharmacy import mpesa
from pharmacy.forms import LoginForm, CustomUserCreationForm, OrderForm
from pharmacy.models import Medication, Order, Customer
from pharmacy.serializers import PaymentSerializer
from utibu_health_pharmacy import settings


# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Medication.objects.all()[:3]
        context = {"products": products}
        return render(request, 'pharmacy/index.html', context)


class StoreView(View):
    def get(self, request):
        products = Medication.objects.all().order_by('-id')
        paginator = Paginator(products, 9)

        page_number = request.GET.get('page')
        page_object = paginator.get_page(page_number)
        context = {"products": products, "page_object": page_object}
        return render(request, 'pharmacy/store.html', context)


class StoreItemView(View):
    def get(self, request, slug, *args, **kwargs):
        product = Medication.objects.get(slug=slug)
        form = OrderForm(initial={'medication': product})
        context = {'product': product, 'form': form}
        return render(request, 'pharmacy/store-item.html', context)

    def post(self, request, slug, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Medication, slug=slug)
            order = form.save(commit=False)
            order.medication = product

            # Check if the user has a customer object
            if hasattr(request.user, 'customer') and request.user.customer:
                order.customer = request.user.customer  # Assign the current user's customer object
                order.save()
                # medication.stock_quantity -= fake_order.quantity
                # product.save()
                return redirect(reverse('confirmation'))  # Redirect to success page or any other page
            else:
                # Display an error message indicating the user has no customer object
                messages.error(request, f'"{request.user}" is not a registered customer.')
                return redirect(reverse('store-item', kwargs={'slug': slug}))
        else:
            product = get_object_or_404(Medication, slug=slug)
            context = {'product': product, 'form': form}
            return render(request, 'pharmacy/store-item.html', context)


class CheckoutView(View):
    pass


class ConfirmationView(View):
    def get(self, request):
        # orders = FakeOrder.objects.all()
        user = request.user.customer
        orders = Order.objects.filter(customer=user)
        order_total = sum(order.total_price for order in orders)
        context = {"orders": orders, "grand_total": order_total}
        return render(request, 'pharmacy/confirmation.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'pharmacy/about.html')


class SignIn(View):
    def get(self, request):
        form = LoginForm
        context = {"form": form}
        # return render(request, 'pharmacy/login.html', context)
        return render(request, 'pharmacy/alt-login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password.')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')

        context = {"form": form}
        # return render(request, 'pharmacy/login.html', context)
        return render(request, 'pharmacy/alt-login.html', context)


def sign_out(request):
    logout(request)
    return redirect('home')


# class SignUp(FormView):
class SignUp(View):
    # template_name = 'pharmacy/sign-up.html'
    # # form_class = UserCreationForm
    # form_class = CustomUserCreationForm
    # success_url = '/'
    #
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def get(self, request):
        form = CustomUserCreationForm()
        context = {"form": form}
        # return render(request, 'pharmacy/sign-up.html', context)
        return render(request, 'pharmacy/alt-sign-up.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save(commit=False)
            user.save()

            # Create Customer instance associated with the user
            phone_number = form.cleaned_data['phone_number']
            customer = Customer.objects.create(user=user, phone_number=phone_number)

            # Authenticate the user after saving the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            context = {"form": form}
            # return render(request, 'pharmacy/sign-up.html', context)
            return render(request, 'pharmacy/alt-sign-up.html', context)


@api_view(['POST'])
def mpesa_payment(request):
    serializer = PaymentSerializer(data=request.data)  # {"phone":"254733444555", "amount": 10}
    if serializer.is_valid(raise_exception=True):
        phone_number = serializer.validated_data["phone"]
        amount = serializer.validated_data["amount"]
        headers = mpesa.generate_request_headers()
        data = {
            "BusinessShortCode": mpesa.get_business_shortcode(),
            "Password": mpesa.generate_password(),
            "Timestamp": mpesa.get_current_timestamp(),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": mpesa.get_business_shortcode(),
            "PhoneNumber": phone_number,
            "CallBackURL": mpesa.get_callback_url(),
            "AccountReference": "Utibu Health Pharmacy",
            "TransactionDesc": "Payment for services"
        }
        resp = requests.post(mpesa.get_payment_url(), json=data, headers=headers)
        print("Response from Safaricom", resp.json())
        return Response({"message": "Initiated STK push"})


@api_view(["POST"])
def mpesa_callback(request):
    data = request.data
    print("Callback from Safaricom", data)
    return Response({"message": "Received Callback"})
