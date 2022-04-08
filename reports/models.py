# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AugmentEntries(models.Model):
    reporting_date = models.DateField()
    path_id = models.IntegerField()
    capacity_added = models.IntegerField()
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'augment_entries'


class AugmentEntryView(models.Model):
    path_id = models.IntegerField(blank=True, null=True)
    reporting_date = models.DateField()
    legacy_company = models.CharField(max_length=6)
    a_location = models.CharField(max_length=50, blank=True, null=True)
    z_location = models.CharField(max_length=50, blank=True, null=True)
    a_node = models.CharField(max_length=50, blank=True, null=True)
    z_node = models.CharField(max_length=50, blank=True, null=True)
    segment_type = models.CharField(max_length=9)
    leased = models.CharField(max_length=5, blank=True, null=True)
    capacity_added_gbps = models.IntegerField()
    ms_capacity_gbps = models.DecimalField(max_digits=33, decimal_places=0, blank=True, null=True)
    ssp_traffic_gbps = models.FloatField(blank=True, null=True)
    wcf_traffic_gbps = models.FloatField(blank=True, null=True)
    pre_aug_ssp_util = models.FloatField(blank=True, null=True)
    pre_aug_wcf_util = models.FloatField(blank=True, null=True)
    post_aug_ssp_util = models.FloatField(blank=True, null=True)
    post_aug_wcf_util = models.FloatField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'augment_entry_view'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CurrentCapacity(models.Model):
    reporting_date = models.DateField()
    current_capacity_gbps = models.IntegerField()
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=10)
    id = models.ForeignKey('Path', db_column='id', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = False
        db_table = 'current_capacity'


class DashboardView(models.Model):
    reporting_date = models.DateField()
    path_id = models.IntegerField()
    legacy_company = models.CharField(max_length=6)
    a_location = models.CharField(max_length=50, blank=True, null=True)
    z_location = models.CharField(max_length=50, blank=True, null=True)
    a_node = models.CharField(max_length=50, blank=True, null=True)
    z_node = models.CharField(max_length=50, blank=True, null=True)
    path_name = models.CharField(max_length=50, blank=True, null=True)
    segment_type = models.CharField(max_length=9)
    leased = models.CharField(max_length=5, blank=True, null=True)
    current_capacity_gbps = models.IntegerField(blank=True, null=True)
    capacity_gbps = models.DecimalField(max_digits=33, decimal_places=0, blank=True, null=True)
    ssp_traffic_gbps = models.FloatField()
    wcf_traffic_gbps = models.FloatField()
    current_ssp_util = models.FloatField(blank=True, null=True)
    current_wcf_util = models.FloatField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'dashboard_view'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.IntegerField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.PositiveIntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    worker = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Location(models.Model):
    location = models.CharField(max_length=50)
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'location'


class Node(models.Model):
    node_name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    legacy_company = models.IntegerField()
    segment = models.IntegerField()
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'node'


class Path(models.Model):
    a_node = models.ForeignKey(Node, related_name='a_node_foreign_key', on_delete=models.CASCADE)
    z_node = models.ForeignKey(Node, related_name='z_node_foreign_key', on_delete=models.CASCADE)
    leased = models.CharField(max_length=5)
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'path'


class PathInfoView(models.Model):
    legacy_company = models.CharField(max_length=6)
    a_location = models.CharField(max_length=50, blank=True, null=True)
    z_location = models.CharField(max_length=50, blank=True, null=True)
    a_node = models.CharField(max_length=50)
    z_node = models.CharField(max_length=50)
    segment_type = models.CharField(max_length=9)
    path_id = models.IntegerField()
    leased = models.CharField(max_length=5)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'path_info_view'


class RestFrameworkTrackingApirequestlog(models.Model):
    requested_at = models.DateTimeField()
    response_ms = models.PositiveIntegerField()
    path = models.CharField(max_length=200)
    remote_addr = models.CharField(max_length=39)
    host = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    query_params = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status_code = models.PositiveIntegerField(blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    view = models.CharField(max_length=200, blank=True, null=True)
    view_method = models.CharField(max_length=27, blank=True, null=True)
    errors = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rest_framework_tracking_apirequestlog'


class TrafficInfo(models.Model):
    reporting_date = models.DateField()
    ssp_traffic_gbps = models.FloatField()
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    wcf_traffic_gbps = models.FloatField()
    created = models.DateTimeField()
    last_updated = models.DateTimeField()
    timestamp = models.DateTimeField()
    user = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'traffic_info'


class UsersBulkpermissionstore(models.Model):
    department = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'users_bulkpermissionstore'


class UsersBulkpermissionstoreGroups(models.Model):
    bulkpermissionstore = models.ForeignKey(UsersBulkpermissionstore, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_bulkpermissionstore_groups'
        unique_together = (('bulkpermissionstore', 'group'),)


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    department = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
