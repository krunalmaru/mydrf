from django.db import models
from rest_framework import serializers

# Create your models here.
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