from django.contrib import admin
from .models import Scan


# Register your models here.
@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('application_name', 'application_link', 'scan_type', 'scan_status', 'scan_date')
    list_filter = ('application_name', 'scan_status', 'scan_date')
    search_fields = ('application_name', 'application_link')
    raw_id_fields = ('scanned_by',)
    date_hierarchy = 'scan_date'
    ordering = ('application_name', 'scan_date')

