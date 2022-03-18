from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	model = CustomUser

# add custom user fields to site admin form
fields = list(CustomUserAdmin.fieldsets)
fields[0] = ("Credentials", {'fields': (
	'username',
	'password',
	'email',
	
)})
fields[1] = ("Personal Info", {'fields': (
	'first_name',
	'last_name',

)})
fields[2] = ("User Type", {'fields': (
	'is_superuser',
	'is_active',
    'is_categoryA',
	'is_categoryB',
	'is_categoryC'
	#Note: is_staff, groups, and user permissions have been removed

)})

CustomUserAdmin.fieldsets = tuple(fields)


# register the new UserAdmin
admin.site.register(CustomUser, CustomUserAdmin)