# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PmCustInsr(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    cid = models.OneToOneField('PmCustmr', models.DO_NOTHING, db_column='cid', primary_key=True)
    ins_no = models.ForeignKey('PmInsrnce', models.DO_NOTHING, db_column='ins_no')

    class Meta:
        managed = True
        db_table = 'pm_cust_insr'
        unique_together = (('cid', 'ins_no'),)


class PmCustmr(models.Model):
    cid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30)
    street = models.CharField(max_length=20)
    h_no = models.IntegerField()
    apt_no = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    zip = models.IntegerField()
    gender = models.CharField(max_length=1, blank=True, null=True)
    mart_status = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'pm_custmr'


class PmDriver(models.Model):
    licence = models.CharField(primary_key=True, max_length=10)
    d_fname = models.CharField(max_length=20)
    d_lname = models.CharField(max_length=20)
    d_mname = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField()
    vin = models.ForeignKey('PmVehcle', models.DO_NOTHING, db_column='vin')

    class Meta:
        managed = True
        db_table = 'pm_driver'


class PmHome(models.Model):
    house_id = models.IntegerField(primary_key=True)
    pur_date = models.DateField()
    pur_value = models.DecimalField(max_digits=10, decimal_places=3)
    area = models.DecimalField(max_digits=7, decimal_places=3)
    htype = models.CharField(max_length=1)
    auto_fire_n = models.CharField(max_length=1)
    home_security = models.CharField(max_length=1)
    basement = models.CharField(max_length=1)
    swim_pool = models.CharField(max_length=1, blank=True, null=True)
    ins_no = models.ForeignKey('PmInHome', models.DO_NOTHING, db_column='ins_no')

    class Meta:
        managed = True
        db_table = 'pm_home'


class PmInAuto(models.Model):
    ins_no = models.OneToOneField('PmInsrnce', models.DO_NOTHING, db_column='ins_no', primary_key=True)

    class Meta:
        managed = True
        db_table = 'pm_in_auto'


class PmInHome(models.Model):
    ins_no = models.OneToOneField('PmInsrnce', models.DO_NOTHING, db_column='ins_no', primary_key=True)

    class Meta:
        managed = True
        db_table = 'pm_in_home'


class PmInsrnce(models.Model):
    ins_no = models.IntegerField(primary_key=True)
    ins_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    prem_amt = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = True
        db_table = 'pm_insrnce'


class PmInvoice(models.Model):
    inv_id = models.IntegerField(primary_key=True)
    inv_date = models.DateField()
    due_date = models.DateField()
    i_amt = models.DecimalField(max_digits=7, decimal_places=2)
    ins_no = models.ForeignKey(PmInsrnce, models.DO_NOTHING, db_column='ins_no')

    class Meta:
        managed = True
        db_table = 'pm_invoice'


class PmPaymnt(models.Model):
    pay_id = models.IntegerField(primary_key=True)
    pay_date = models.DateField()
    method = models.CharField(max_length=2)
    p_amt = models.DecimalField(max_digits=7, decimal_places=2)
    inv = models.ForeignKey(PmInvoice, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'pm_paymnt'


class PmVehcle(models.Model):
    vin = models.IntegerField(primary_key=True)
    vmake = models.CharField(max_length=20)
    vmodel = models.CharField(max_length=10)
    model_yr = models.IntegerField()
    status = models.CharField(max_length=1)
    ins_no = models.ForeignKey(PmInAuto, models.DO_NOTHING, db_column='ins_no')

    class Meta:
        managed = True
        db_table = 'pm_vehcle'

class InsertCustRec(models.Model):
    firstname = models.CharField(max_length = 30)
    middlename = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    street = models.CharField(max_length = 20)
    house_no = models.IntegerField()
    apt_no = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    zip = models.IntegerField()
    gender = models.CharField(max_length = 1)
    mart_status = models.CharField(max_length = 1)


class InsertInsurance(models.Model):
    cid = models.IntegerField()
    insurance_type = models.CharField(max_length = 1)
    status = models.CharField(max_length = 1)
    premium = models.IntegerField()
    startdate = models.DateField()
    enddate = models.DateField()

class InsertVehicle(models.Model):
    vin = models.IntegerField()
    vmake = models.CharField(max_length = 20)
    vmodel = models.CharField(max_length = 10)
    model_yr = models.IntegerField()
    status = models.CharField(max_length = 1)
    ins_no = models.IntegerField()

class InsertDriver(models.Model):
    licence = models.CharField(max_length = 10)
    d_fname = models.CharField(max_length = 20)
    d_lname = models.CharField(max_length = 20)
    d_mname = models.CharField(max_length = 20)
    birthdate = models.DateField()
    vin = models.IntegerField()

class InsertHome(models.Model):
    pur_date = models.DateField()
    pur_value = models.IntegerField()
    area = models.IntegerField()
    htype = models.CharField(max_length = 1)
    auto_fire_n = models.CharField(max_length = 1)
    home_security = models.CharField(max_length = 1)
    basement = models.CharField(max_length = 1)
    swim_pool = models.CharField(max_length = 1)
    ins_no = models.IntegerField()

class InsuranceRecord(models.Model):
    ins_no = models.IntegerField()
    ins_type = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    prem_amt = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    cid = models.IntegerField()

# class UpdatePmCustmr(models.Model):
#     cid = models.IntegerField(primary_key=True)
#     fname = models.CharField(max_length=30)
#     mname = models.CharField(max_length=30, blank=True, null=True)
#     lname = models.CharField(max_length=30)
#     street = models.CharField(max_length=20)
#     h_no = models.IntegerField()
#     apt_no = models.CharField(max_length=10, blank=True, null=True)
#     city = models.CharField(max_length=20)
#     state = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)
#     zip = models.IntegerField()
#     gender = models.CharField(max_length=1, blank=True, null=True)
#     mart_status = models.CharField(max_length=1)
#
#     class Meta:
#         # managed = True
#         db_table = 'pm_custmr'



