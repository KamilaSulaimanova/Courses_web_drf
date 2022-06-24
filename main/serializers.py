from rest_framework import serializers
from .models import Student, Mentor, Course, CourseFlow


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['user',]


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
        read_only_fields = ['user',]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFlow
        fields = '__all__'