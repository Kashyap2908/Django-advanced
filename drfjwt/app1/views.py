from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.permissions import BasePermission
from .serializers import EmpSerializer
from rest_framework.decorators import api_view
from .models import Emp
from rest_framework.response import Response
# Create your views here.
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','HEAD','OPTIONS']:
            return True
        return request.user.is_staff
        
class EmpViewSet(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer
    permission_classes=[IsAdminOrReadOnly]

# @api_view(['GET'])
# def get_emp(req):
#     e=Emp.objects.all()
#     serializer=EmpSerializer(e,many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_emp(req):
#     serializer=EmpSerializer(data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def emp_detail(req,id):
#     try:
#         emp=Emp.objects.get(id=id)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if req.method=='GET':
#         serializer=EmpSerializer(emp)
#         return Response(serializer.data)
#     elif req.method=='POST':
#         serializer=EmpSerializer(emp,data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif req.method=='DELETE':
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)