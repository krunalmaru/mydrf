from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer,UserSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        return JsonResponse({'message':'Succesfully'})

def UserListView(request):
    usr = User.objects.all()
    serializer = UserSerializer(usr, many=True)
    return JsonResponse(serializer.data, safe=False)