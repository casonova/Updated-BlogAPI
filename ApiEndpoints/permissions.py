from rest_framework import permissions


class IsLoggedIn(permissions.BasePermission):
    """Permission for Authenticated user"""

    def has_permission(
        self,
        request,
        view,
    ):
        return request.user and request.user.is_active and request.user.is_staff

    def has_object_permission(
        self,
        request,
        view,
        obj):
        return request.user and request.user.is_active and request.user.is_staff
