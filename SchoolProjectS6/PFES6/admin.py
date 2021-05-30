from django.contrib import admin
#from .models import EmployeeDetails
# Register your models here.
from .models import Users



class UsersAdmin(admin.ModelAdmin) :
    list_display  = ('nom','prenom','email','password','picture','role')

admin.site.register(Users,UsersAdmin)