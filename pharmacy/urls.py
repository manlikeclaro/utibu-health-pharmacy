from django.urls import path, include

from pharmacy import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('store', views.StoreView.as_view(), name='store'),
    path('store/<slug:slug>', views.StoreItemView.as_view(), name='store-item'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('confirmation', views.ConfirmationView.as_view(), name='confirmation'),
    path('about', views.AboutView.as_view(), name='about'),
    path('login', views.SignIn.as_view(), name='login'),
    path('logout', views.sign_out, name='logout'),
    path('sign-up', views.SignUp.as_view(), name='sign-up'),

    # Mpesa api paths
    path('mpesa-payment', views.mpesa_payment, name='mpesa-payment'),
    path('mpesa-callback', views.mpesa_callback, name='mpesa-callback'),

    # Include API URLs
    path('api/', include('pharmacy.api.urls')),
]
