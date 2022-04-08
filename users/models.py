""" models related to user management functions """

from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    """ Main user model for the project """

    # department of the user
    department = models.CharField(max_length=255, null=True, blank=True)

    # telephone number of the user
    telephone = models.CharField(max_length=255, null=True, blank=True)

    # job title
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """ string representation of the user """

        return '%s, %s' % (self.last_name, self.first_name)

    def full_rep(self):
        """ full string representation of the user """

        return '%s, %s <%s>' % (self.last_name, self.first_name, self.email)

    @property
    def permissions(self):
        """ what permissions / roles does this user have """

        bps, _ = BulkPermissionStore.objects.get_or_create(
            department=self.department
        )

        if self.is_superuser is True:
            my_groups = Group.objects.all().values_list('name', flat=True)
            bps_groups = []
        else:
            my_groups = self.groups.all().values_list('name', flat=True)
            bps_groups = bps.groups.all().values_list('name', flat=True)

        all_groups = list(set(list(my_groups) + list(bps_groups)))

        return {group: True for group in all_groups}


class BulkPermissionStore(models.Model):
    """ bulk permissions grant roles to departments """

    # department the groups apply to
    department = models.CharField(max_length=255, unique=True)

    # what roles does this department have
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        """ string representation """

        return self.department
