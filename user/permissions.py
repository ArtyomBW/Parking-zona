from rest_framework.permissions import BasePermission

from user.models import User


class IsAdmin(BasePermission):
    message = "Sizda AMIN huquqi yoq mon ami !"
    def has_permission(self, request, view):
        return request.user.role == User.RoleType.ADMIN.value
