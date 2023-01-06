from .models import Employee
from django.contrib.auth.models import User
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=70)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)