from django.contrib import admin
from .models import Course,MyCourse,Instructor
# Register your models here.

admin.site.register(Course)
admin.site.register(MyCourse)
admin.site.register(Instructor)