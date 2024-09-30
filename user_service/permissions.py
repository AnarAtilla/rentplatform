from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Кастомное разрешение, позволяющее редактировать объект только его владельцам.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение для любого запроса
        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверка на то, что пользователь является владельцем объекта
        return obj.owner == request.user

class IsActiveUser(permissions.BasePermission):
    """
    Разрешение для проверки, активен ли пользователь.
    """
    def has_permission(self, request, view):
        # Проверяем, активен ли пользователь
        return request.user.is_authenticated and request.user.status == 'active'

class IsAdminUser(permissions.BasePermission):
    """
    Разрешение, дающее доступ только администраторам.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
