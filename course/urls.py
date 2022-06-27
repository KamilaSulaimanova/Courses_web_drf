from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from main.views import CourseViewSet, CourseFlowViewSet

router = DefaultRouter()

router.register('course', CourseViewSet, basename='course')
router.register('course-flow', CourseFlowViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += [path
        ('', include('rest_framework.urls')),
    ]