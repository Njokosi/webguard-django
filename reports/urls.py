from django.urls import path
from reports.views import ReportListView

app_name = 'reports'

urlpatterns = [
    # report views
    path('', ReportListView.as_view(), name='report-list'),
]
