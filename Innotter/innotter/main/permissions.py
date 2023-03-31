from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return bool(request.user.role == 'admin' or request.user.is_staff)
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.owner == request.user or request.user and request.user.is_staff)


class IsPostOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(obj.page.owner == request.user or request.user and request.user.is_staff)
