from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

# Job list api view
class JobListView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

# Job detail api view 
class JobDetailView(APIView):
    def get(self, request, id):
        try:
            job = Job.objects.get(id=id)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)
        return Response(serializer.data)