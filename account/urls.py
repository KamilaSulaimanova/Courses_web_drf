from re import S
from django.urls import path, include
from django.conf import settings
from .views import StudentCreateAPIView, MentorCreateAPIView

urlpatterns = [
    path('create/student/', StudentCreateAPIView.as_view(), name='create_student'),
    path('create/mentor/', MentorCreateAPIView.as_view(), name='create_mentor'),
]