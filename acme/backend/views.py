from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class VetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Vet.objects.all()
    serializer_class = VetSerializer

class CashierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cashier.objects.all()
    serializer_class = CashierSerializer

class PetViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows groups to be viewed or edited.
        """
        queryset = Pet.objects.all()
        serializer_class = PetSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class RecordViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows groups to be viewed or edited.
        """
        queryset = Record.objects.all()
        serializer_class = RecordSerializer


class BillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows groups to be viewed or edited.
        """
        queryset = Administrator.objects.all()
        serializer_class = AdministratorSerializer


