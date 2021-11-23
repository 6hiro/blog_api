from rest_framework import permissions


class IsOwnPostOrReadOnly(permissions.BasePermission):
    """Allow user to edit their own post"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own post"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.posted_by == request.user
