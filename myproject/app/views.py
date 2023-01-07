from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Employee
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer,UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
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
def employeeDetailView(request, pk):
    
    try:
        employee = Employee.objects.get(pk=pk)
        # return JsonResponse('employee:'+str(pk),safe=False)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status= status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'PUT':
        jsondata = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors)




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
