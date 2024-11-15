from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DepartmentPerformanceReport

class DepartmentPerformanceReportView(APIView):
    def get(self, request):
        performance_data = DepartmentPerformanceReport.get_performance_data()
        return Response(performance_data, status=status.HTTP_200_OK)
