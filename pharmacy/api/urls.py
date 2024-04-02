from django.urls import path
from .views import (
    APIRootView,
    MedicationListCreateAPIView,
    MedicationRetrieveUpdateDestroyAPIView,
    CustomerListCreateAPIView,
    CustomerRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('medications/', MedicationListCreateAPIView.as_view(), name='medication-list-create'),
    path('medications/<int:pk>/', MedicationRetrieveUpdateDestroyAPIView.as_view(), name='medication-detail'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
]
