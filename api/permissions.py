from rest_framework import permissions

def user_has_group(user, group_name):
    """
    user_has_group returns true if user is member of group_name or 'SUPERUSER'
    """
    try:
        my_permissions = user.permissions
    except:
        # must be AnonymousUser
        my_permissions = []
    return any(group in my_permissions for group in (group_name, 'SUPERUSER'))

class UserHasAdmin(permissions.BasePermission):
    """ just an example, return true if use has ADMIN group """

    def has_permission(self, request, view):
        """ just an example, return true if use has ADMIN group """

        return user_has_group(request.user, 'ADMIN')
