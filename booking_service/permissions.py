from rest_framework import permissions


class IsGuestOrReadOnly(permissions.BasePermission):
    """
    Разрешение только для гостя, который создал бронирование.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить изменения только гостю, который сделал бронирование
        return obj.guest == request.user
