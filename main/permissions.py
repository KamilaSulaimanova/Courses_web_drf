from rest_framework.permissions import BasePermission, SAFE_METHODS


class CoursePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return request.user.is_superuser or request.user.mentor
        

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.is_authenticated:    
                return True
        if request.user.is_superuser:
            return True
        if request.user == obj.mentor:
            return True


class CourseFlowPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if request.user.is_authenticated:    
                return True
        return request.user.is_superuser