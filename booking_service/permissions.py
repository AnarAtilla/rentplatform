from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Кастомное разрешение, позволяющее управлять объектом только его владельцам.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверяем, что текущий пользователь является владельцем бронирования
        return obj.guest == request.user
