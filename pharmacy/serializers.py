from rest_framework import serializers

from .models import Medication, Customer, Order


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class MedicationGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class MedicationPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        exclude = ('short_description', 'slug')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
