from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Employee
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer,UserSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def employeeListView(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(jsonData)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        # return JsonResponse('employee:'+str(pk),safe=False)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET','POST'])
def UserListView(request):
    if request.method == 'GET':
        usr = User.objects.all()
        serializer = UserSerializer(usr, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

