from dataclasses import fields
from rest_framework import serializers
from .models import User
from main.models import Student, Mentor
from main.serializers import StudentSerializer, MentorSerializer


class UserCreteSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128)


    def vaidate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords should match')
        return data



class StudentCreateSerializer(UserCreteSerializer):
    student = StudentSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'student',]

    def save(self, ):
        user = User(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        try:
            student = Student(user=user, name=self.validated_data['student']['name'])
            student.save()
        except Exception as e:
            print(e)
            user.delete()
        else:
            return user


class MentorCreateSerializer(UserCreteSerializer):
    mentor = MentorSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'mentor',]

    def save(self):
        user = User(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        try:
            mentor = Mentor(user=user, name=self.validated_data['mentor']['name'])
            mentor.save()
        except Exception as e:
            print(e)
            user.delete()
        else:
            return user
