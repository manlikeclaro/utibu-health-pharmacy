from django.urls import path, include

from pharmacy import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('store', views.StoreView.as_view(), name='store'),
    path('store/<int:item_id>', views.StoreItemView.as_view(), name='store-item'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('confirmation', views.ConfirmationView.as_view(), name='confirmation'),
    path('about', views.AboutView.as_view(), name='about'),
]
