from django.contrib import admin

from .models import Application


# Register your models here.
@admin.register(Application)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('application_name', 'application_link', 'scan_type')
    list_filter = ('application_name', 'scan_type')
    search_fields = ('application_name', 'application_link')
    date_hierarchy = 'created'
    ordering = ('application_name',)
