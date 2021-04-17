from django.db import models
from django.utils import timezone
# import os
# import json
import uuid

# Choices fields
from .choices.scan import scan_category


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='scan_date')
    scan_category = models.CharField(max_length=30, choices=scan_category, default='light_scan')
    scan_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Reports"
        ordering = ('-scan_date',)

    def __str__(self):
        return self.title
