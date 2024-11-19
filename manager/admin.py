from django.contrib import admin
from .models import Manager

# Register your models here.
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone_number', 'designation', 'email', 'date_of_birth', 'gender', 'status')

admin.site.register(Manager, ManagerAdmin)
