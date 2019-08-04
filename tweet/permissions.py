from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    def has_object_permmission(self, request, view, obj):
        return obj.author == request.user

class IsOwnerAndAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_superuser

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # 원하는 반환값으로 설정
        return obj.author == request.user or request.user.is_superuser