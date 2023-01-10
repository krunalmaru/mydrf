from rest_framework import serializers
from .models import MyCourse,Instructor,Course


class MyCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyCourse
        fields = '__all__'


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(read_only = True,many=True,view_name='mycourse-detail')

    class Meta:
        model = Instructor
        fields = '__all__'











class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"