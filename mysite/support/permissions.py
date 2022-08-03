from rest_framework import permissions


# кастомный уровень доступа для представления на удаленине заявки
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
