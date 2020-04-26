from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Blob, Floors, Projects

admin.site.register(User, UserAdmin)
admin.site.register(Blob)
admin.site.register(Floors)
admin.site.register(Projects)


# Register your models here.
