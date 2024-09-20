from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение только для владельца отзыва
    """
    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ на чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверяем, что пользователь является владельцем отзыва
        return obj.guest == request.user
