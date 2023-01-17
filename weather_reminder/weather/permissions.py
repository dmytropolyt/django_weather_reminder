from rest_framework import permissions


class IsAdminOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            ((request.method in permissions.SAFE_METHODS or request.method in 'POST') and
             request.user and
             request.user.is_authenticated) or
            (request.user and
             request.user.is_authenticated and
             request.user.is_staff)
        )


class IsOwnerOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
