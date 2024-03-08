from rest_framework import permissions

class IsSuperUserAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            if request.user.is_superuser and request.user.is_authenticated:
                return True
            return False
        return True

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False