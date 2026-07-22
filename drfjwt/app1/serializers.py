from .models import Emp
from rest_framework import serializers

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'
        