from django.urls import path,include
from apps.views import InstructorListView,MyCoursesListview


urlpatterns = [
    # path('course/', views.CourseListView.as_view(), name='courselist'),
    # path('course/<int:pk>', views.CorseDetailView.as_view(),name='cousedetail'),
    path('instructor/',InstructorListView.as_view(),name='instructor'),
    path('mycourses/', MyCoursesListview.as_view(),name='mycourses' )
]
