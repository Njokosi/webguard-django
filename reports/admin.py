from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'scan_date')
    prepopulated_fields = {'slug': ('title',)}
