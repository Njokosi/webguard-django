from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView

from .models import Report


# Create your views here.

class ReportListView(ListView):
    model = Report

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        # template_name = 'reports/report_list.html'
        return context
