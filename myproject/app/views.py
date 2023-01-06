from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer,UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            # print(jsonData)
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
@csrf_exempt
def UserListView(request):
    if request.method == 'GET':
        usr = User.objects.all()
        serializer = UserSerializer(usr, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        jsondata = JSONParser().parse(request)
        serializer = UserSerializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)