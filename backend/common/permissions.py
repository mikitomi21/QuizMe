from rest_framework import permissions


class CustomPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

