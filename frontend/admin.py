from django.contrib import admin
from django.db import models
from frontend.models import *
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin


class ProfileInline(admin.StackedInline):
    """ As you are noticed your profile will be edited as inline form """
    model = Profile
    can_delete = False
 
class UserAdmin(OriginalUserAdmin):
    """ Just add inlines to the original UserAdmin class """
    inlines = [ProfileInline, ]
 
try:
    admin.site.unregister(User)
finally:
    admin.site.register(User, UserAdmin)

admin.site.register(Profile)