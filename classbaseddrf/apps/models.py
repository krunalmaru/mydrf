from django.db import models
from rest_framework import serializers

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email

class MyCourse(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,related_name='courses')


class MyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourse
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    courses = MyCourseSerializer(read_only = True,many=True)

    class Meta:
        model = Instructor
        fields = '__all__'


class Course(models.Model):
    name= models.CharField(max_length=70)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.DurationField()
    authorname = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"