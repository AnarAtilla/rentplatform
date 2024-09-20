from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Разрешение только для администраторов на изменение данных.
    Остальные могут только читать.
    """

    def has_permission(self, request, view):
        # Разрешаем доступ на чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True
        # Для изменения данных проверяем, что пользователь — администратор
        return request.user and request.user.is_staff



class IsAuthenticatedUser(permissions.BasePermission):
    """
    Разрешение только для аутентифицированных пользователей.
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        return request.user and request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение только владельцам данных на их изменение.
    Остальные могут только читать.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ на чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True
        # Проверяем, что пользователь является владельцем записи
        return obj.user == request.user

