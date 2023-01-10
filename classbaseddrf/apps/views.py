from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course,Instructor,MyCourse
from django.http import Http404
from rest_framework import status
from rest_framework import mixins, generics
from .serializer import CourseModelSerializer,InstructorSerializer,MyCourseSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission,BasePermissionMetaclass
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
# Create your views here.
# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        print("permisiion user is:", request.user)
        user = request.user
        if request.method == 'GET':
            return True
        if request.method == 'POST' or request.method=='PUt' or request.method =='DELETE':
            if user.is_superuser:
                return True
        
        return False



class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class MyCoursesListview(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    serializer_class = MyCourseSerializer
    queryset = MyCourse.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyCourseSerializer
    queryset = MyCourse.objects.all()


# class CourseViewSet(ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseModelSerializer

'''
class CourseViewSet(ViewSet):
    def list(self,request):
        courses = Course.objects.all()
        serializer = CourseModelSerializer(courses, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = CourseModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk):
        try:
            course=Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CourseModelSerializer(course) 
        return Response(serializer.data)       

    def destroy(self, request,pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request,pk):
        course = Course.objects.get(pk=pk)
        serialize = CourseModelSerializer(course, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
'''



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
# class CourseListView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseModelSerializer

# class CorseDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseModelSerializer


# class CorseDetailView(generics.RetrieveDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseModelSerializer

# class CorseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseModelSerializer


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
        