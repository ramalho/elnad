# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Department(models.Model):
    dname = models.CharField(max_length=75)
    dnumber = models.IntegerField(primary_key=True)
    mgrssn = models.CharField(max_length=27)
    mgrstartdate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'department'

class Dependent(models.Model):
    essn = models.CharField(max_length=27, primary_key=True)
    dependent_name = models.CharField(max_length=45, primary_key=True)
    sex = models.CharField(max_length=3, blank=True)
    bdate = models.DateField(null=True, blank=True)
    relationship = models.CharField(max_length=24, blank=True)
    class Meta:
        db_table = u'dependent'

class DeptLocations(models.Model):
    dnumber = models.IntegerField(primary_key=True)
    dlocation = models.CharField(max_length=45, primary_key=True)
    class Meta:
        db_table = u'dept_locations'

class Employee(models.Model):
    fname = models.CharField(max_length=45)
    minit = models.CharField(max_length=3, blank=True)
    lname = models.CharField(max_length=45)
    ssn = models.CharField(max_length=27, primary_key=True)
    bdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=150, blank=True)
    sex = models.CharField(max_length=3, blank=True)
    salary = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    superssn = models.CharField(max_length=27, blank=True)
    dno = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'employee'

class Project(models.Model):
    pname = models.CharField(unique=True, max_length=75)
    pnumber = models.IntegerField(primary_key=True)
    plocation = models.CharField(max_length=45, blank=True)
    dnum = models.IntegerField()
    class Meta:
        db_table = u'project'

class WorksOn(models.Model):
    essn = models.CharField(max_length=27, primary_key=True)
    pno = models.IntegerField()
    hours = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    class Meta:
        db_table = u'works_on'

