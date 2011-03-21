from django.contrib import admin
from elnad.company.models import (Department, Dependent, DeptLocations,
    Employee, Project, WorksOn)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dnumber', 'dname', 'mgrssn')

class DependentAdmin(admin.ModelAdmin):
    list_display = ('essn', 'dependent_name')

class DeptLocationsAdmin(admin.ModelAdmin):
    list_display = ('dnumber', 'dlocation')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'lname', 'fname')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'lname', 'fname')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pnumber', 'pname')

class WorksOnAdmin(admin.ModelAdmin):
    list_display = ('essn', 'pno')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Dependent, DependentAdmin)
admin.site.register(DeptLocations, DeptLocationsAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(WorksOn, WorksOnAdmin)
