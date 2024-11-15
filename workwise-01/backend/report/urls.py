from django.urls import path
from .views import DepartmentPerformanceReportView

urlpatterns = [
    path('department-performance/', DepartmentPerformanceReportView.as_view(), name='department_performance_report')
]
