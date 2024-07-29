from django.contrib import admin
from .models import *

'''
class ExampleAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('id', 'name', 'description')
    
    # Specify the fields to search by
    search_fields = ('id', 'name', 'description')
    
    # Specify the filters to use in the list view
    list_filter = ('id', 'name', 'description')

admin.site.register(Example, ExampleAdmin)
'''