from rest_framework import permissions


class TutorPermissions(permissions.BasePermission):
    """Права доступа для только для кураторов"""
    def has_permission(self, request, view):
        return request.user.is_tutor


class AdminPermissions(permissions.BasePermission):
    """Права доступа для только для администраторов"""
    def has_permission(self, request, view):
        if request.user.is_tutor == False and request.user.is_superuser == True:
            return True
