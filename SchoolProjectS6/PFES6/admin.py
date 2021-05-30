from django.contrib import admin
from .models import Users

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password', 'picture', 'role')


admin.site.register(Users, UsersAdmin)
