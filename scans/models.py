from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .choices import scan


# Create your models here.
class Scan(models.Model):
    application_name = models.CharField(max_length=50)
    application_link = models.URLField(max_length=200)
    scan_type = models.CharField(max_length=30, choices=scan.scan_category, default='light_scan')
    scan_status = models.CharField(max_length=30, choices=scan.status, default='not_initiated')
    scan_date = models.DateTimeField(default=timezone.now)
    scanned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_scans')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.application_name

    class Meta:
        verbose_name_plural = "Scan reports"
        ordering = ('-scan_date',)
