from django.db import models
from django.utils import timezone

from .choices import scan


# Create your models here.
class Application(models.Model):
    application_name = models.CharField(max_length=50)
    application_link = models.URLField(max_length=200)
    scan_type = models.CharField(max_length=30, choices=scan.scan_category, default='light_scan')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.application_name

    class Meta:
        verbose_name_plural = "Web applications"
        ordering = ('-application_name',)
