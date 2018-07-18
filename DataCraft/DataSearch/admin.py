from django.contrib import admin
from .models import Client
from .models import PublishserData,Department,SubDepartment
admin.site.register(Client)
admin.site.register(PublishserData)
admin.site.register(Department)
admin.site.register(SubDepartment)


