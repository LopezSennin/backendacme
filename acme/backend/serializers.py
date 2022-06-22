from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url','id_number', 'first_name', 'last_name', 'address','phone_number','email']

class VetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vet
        fields = ['url','id_number', 'first_name', 'last_name', 'address','phone_number','email', 'password']

class CashierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cashier
        fields = ['url','id_number', 'first_name', 'last_name', 'address','phone_number','email', 'password']


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ['url','id_pet', 'full_name', 'sex', 'birth_date','animal_type','owner']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['url','id_service', 'description', 'cost', 'state']

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['url','id_record', 'description', 'date', 'vet', 'service', 'pet', 'state']

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = ['url','id_bill', 'record', 'cost']

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Administrator
        fields = ['url','user', 'password']


