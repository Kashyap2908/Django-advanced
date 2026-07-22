from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from .permission import IsAdminOrReadonly

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    permission_classes=[IsAdminOrReadonly]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    permission_classes=[IsAdminOrReadonly]
