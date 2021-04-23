from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display =['full_name','email',"mobile"]