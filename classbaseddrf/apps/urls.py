from django.urls import path
from apps import views

urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='courselist'),
    path('course/<int:pk>', views.CorseDetailView.as_view(),name='cousedetail'),
]
