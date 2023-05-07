from django.contrib import admin
from .models import *


# Register your models here.
class StatesAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Is_Union_Territory']
admin.site.register(States, StatesAdmin)

class DistrictsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'state']
admin.site.register(Districts, DistrictsAdmin)