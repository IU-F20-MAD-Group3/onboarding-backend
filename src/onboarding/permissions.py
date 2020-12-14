from rest_framework import permissions


class IsMember(permissions.BasePermission):
    """Checks whether a user is a member of any organization.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'member')
