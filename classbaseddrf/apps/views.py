from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course,CourseModelSerializer
from django.http import Http404
from rest_framework import status
from rest_framework import mixins, generics
# Create your views here.


'''########## listApiview = listmodelmixin + genericApiView ###########'''
'''########## generics = get ,post,put,delete ############'''

'''
class CourseListView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

class CorseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

'''
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

# class CorseDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseModelSerializer


class CorseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

'''
class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
'''

'''
    class CorseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
        queryset = Course.objects.all()
        serializer_class = CourseModelSerializer

        def get(self,request,pk):
            return self.retrieve(request,pk)

        def delete(self, request,pk):
            return self.destroy(request,pk)

        def put(self, request,pk):
            return self.update(request,pk)
'''

# class CourseListView(APIView):
#     def get(self, request):
#         cou = Course.objects.all()
#         serializer = CourseModelSerializer(cou, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CourseModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

# class CorseDetailView(APIView):
#     def get_course(self,pk):
#         try:
#            return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         course = self.get_course(pk)
#         serializer = CourseModelSerializer(course)
#         return Response(serializer.data)
#     # def post(self,request,pk):
#     #     serialiser = CourseModelSerializer(data=request.data)
#     #     if serialiser.is_valid():
#     #         serialiser.save()
#     #         return Response(serialiser.data)
#     #     return Response(serialiser.errors)

#     def delete(self,request,pk):
#         course = self.get_course(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
       
#     def put(self,request,pk):
#         course = self.get_course(pk)
#         serializer = CourseModelSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
        