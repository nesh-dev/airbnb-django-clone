from django.contrib import admin
from . models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class UserProfileInline(admin.StackedInline):
  model = UserProfile
  can_delete = False
  

class UserAdmin(BaseUserAdmin):
    inlines = (
      UserProfileInline,
       )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


