from django.contrib import admin
from .models import Employee,Voter,Admin1,Contender,Count,votervotemapping
# # Register your models here.
admin.site.register(Employee)
admin.site.register(Voter)
admin.site.register(Admin1)
admin.site.register(Contender)
admin.site.register(Count)
admin.site.register(votervotemapping)
# employee.site.register(FacultyCourseMapping)
