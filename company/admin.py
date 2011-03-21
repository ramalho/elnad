from django.contrib import admin
from elnad.company.models import (Department, Dependent, DeptLocations,
    Employee, Project, WorksOn)

admin.site.register(Department)
admin.site.register(Dependent)
admin.site.register(DeptLocations)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(WorksOn)
