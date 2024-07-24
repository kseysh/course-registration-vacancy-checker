from django.contrib import admin
from .models import *

class SearchAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name', 'major_name']
    
admin.site.register(Course, SearchAdmin)

