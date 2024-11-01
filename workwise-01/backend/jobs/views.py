from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

class JobListView(APIView):
    """
    API view to retrieve a list of all jobs.

    This view provides a GET method that retrieves all instances of the Job model
    and serializes them using JobSerializer. The serialized data is returned as a response.
    """

    def get(self, request):
        """
        Handle GET requests to retrieve a list of jobs.

        Returns:
            Response: JSON representation of the list of jobs.
        """
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class JobDetailView(APIView):
    """
    API view to retrieve a single job by its ID.

    This view provides a GET method that retrieves a specific instance of the Job model
    based on the provided ID. If the job does not exist, it returns a 404 status.
    """

    def get(self, request, id):
        """
        Handle GET requests to retrieve a specific job by ID.

        Args:
            request: The HTTP request object.
            id (int): The ID of the job to retrieve.

        Returns:
            Response: JSON representation of the job details if found, otherwise a 404 status.
        """
        try:
            job = Job.objects.get(id=id)
        except Job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)
        return Response(serializer.data)
