from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course,CourseModelSerializer
# Create your views here.

class CourseListView(APIView):
    def get(self, request):
        cou = Course.objects.all()
        serializer = CourseModelSerializer(cou, many=True)
        return Response(serializer.data)