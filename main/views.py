from django.shortcuts import render
from .models import Course, CourseFlow
from .serializers import CourseSerializer, CourseFlowSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, authentication


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.BasePermission,]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication, ]



class CourseFlowViewSet(ModelViewSet):
    queryset = CourseFlow.objects.all()
    serializer_class = CourseFlowSerializer
    permission_classes = [permissions.BasePermission,]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication, ]



