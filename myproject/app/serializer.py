from .models import Employee
from django.contrib.auth.models import User
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    # name= serializers.CharField(max_length=100)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=100)
    # phone = serializers.CharField(max_length=20)

    # def create(self, validated_data):
    #     print("create method called")
    #     return Employee.objects.create(**validated_data)

    # def update(self, employee, validated_data):
    #     newemployee = Employee(**validated_data)
    #     newemployee.id = employee.id
    #     newemployee.save()
    #     return newemployee
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    # username = serializers.CharField(max_length=70)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=20)
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)

    # def create(self, validated_data):
    #     print("user saved")
    #     return User.objects.create(**validated_data)