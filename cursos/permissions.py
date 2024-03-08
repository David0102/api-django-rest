from rest_framework import permissions

class IsSuperUserAuthNotPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'POST':
            if request.user.is_superuser and request.user.is_authenticated:
                return True
            return False
        return True

class IsSuperUserAuthNotGet(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method != 'GET':
            if request.user.is_superuser and request.user.is_authenticated:
                return True
            return False
        return True