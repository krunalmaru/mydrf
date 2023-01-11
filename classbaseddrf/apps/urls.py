from django.urls import path,include
from apps.views import InstructorListView,MyCoursesListview,CourseDetailView,InstructorDetailView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
urlpatterns = [
    # path('course/', views.CourseListView.as_view(), name='courselist'),
    # path('course/<int:pk>', views.CorseDetailView.as_view(),name='cousedetail'),
    path('instructor/',InstructorListView.as_view(),name='instructor'),
    path('instructor/<int:pk>',InstructorDetailView.as_view(),name='instructor-detail'),
    path('mycourses/', MyCoursesListview.as_view(),name='mycourses' ),
    path('mycourses/<int:pk>',CourseDetailView.as_view(),name='mycourse-detail' ),
    # path('auth/login/',obtain_auth_token,name='create-token' ),
    path('auth/login/',TokenObtainPairView.as_view(),name='create-token' ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),




]
