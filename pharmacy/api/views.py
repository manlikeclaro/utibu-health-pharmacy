from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from pharmacy.models import Medication, Customer, Order
from pharmacy.serializers import MedicationSerializer, CustomerSerializer, OrderSerializer, MedicationPOSTSerializer, \
    MedicationGETSerializer


# Class-based views for listing and creating Medication instances
class APIRootView(APIView):
    def get(self, request, format=None):
        # Generate a dictionary containing the available paths and their corresponding URLs
        paths = {
            'medications': reverse('medication-list-create', request=request, format=format),
            'medication_detail': reverse('medication-detail', kwargs={'pk': 1}, request=request, format=format),
            # assuming there's at least one medication
            'customers': reverse('customer-list-create', request=request, format=format),
            'customer_detail': reverse('customer-detail', kwargs={'pk': 1}, request=request, format=format),
            # assuming there's at least one customer
            'orders': reverse('order-list-create', request=request, format=format),
            'order_detail': reverse('order-detail', kwargs={'pk': 1}, request=request, format=format),
            # assuming there's at least one order
        }
        return Response(paths)


# class MedicationListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Medication.objects.all()  # Retrieve all Medication instances
#     serializer_class = MedicationSerializer  # Serializer class to convert queryset to JSON and vice versa
#
#
# # Class-based views for retrieving, updating, and deleting Medication instances
# class MedicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Medication.objects.all()  # Retrieve all Medication instances
#     serializer_class = MedicationSerializer  # Serializer class to convert queryset to JSON and vice versa

# Customization Start
class MedicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MedicationPOSTSerializer
        return MedicationGETSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medication.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return MedicationPOSTSerializer
        return MedicationGETSerializer


# Customization End


# Class-based views for listing and creating Customer instances
class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()  # Retrieve all Customer instances
    serializer_class = CustomerSerializer  # Serializer class to convert queryset to JSON and vice versa


# Class-based views for retrieving, updating, and deleting Customer instances
class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()  # Retrieve all Customer instances
    serializer_class = CustomerSerializer  # Serializer class to convert queryset to JSON and vice versa


# Class-based views for listing and creating Order instances
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()  # Retrieve all Order instances
    serializer_class = OrderSerializer  # Serializer class to convert queryset to JSON and vice versa


# Class-based views for retrieving, updating, and deleting Order instances
class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()  # Retrieve all Order instances
    serializer_class = OrderSerializer  # Serializer class to convert queryset to JSON and vice versa
