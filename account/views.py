from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import StudentCreateSerializer, MentorCreateSerializer
from .models import User


class UserCreteAPIView(CreateAPIView):
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
        }, status=status.HTTP_201_CREATED, headers=headers)


class StudentCreateAPIView(UserCreteAPIView):
    serializer_class = StudentCreateSerializer

    
class MentorCreateAPIView(UserCreteAPIView):
    serializer_class = MentorCreateSerializer
