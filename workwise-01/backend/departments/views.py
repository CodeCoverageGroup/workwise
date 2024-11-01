# pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Department instances.

    This ViewSet provides CRUD operations for the Department model,
    allowing authenticated users with JWT-based authentication to
    create, retrieve, update, and delete department records.
    """

    queryset = Department.objects.all()
    """Defines the base queryset for retrieving Department records."""

    serializer_class = DepartmentSerializer
    """Specifies the serializer used to validate and serialize Department data."""

    authentication_classes = [JWTAuthentication]
    """Enforces JWT authentication for accessing this ViewSet."""

    permission_classes = [IsAuthenticated]
    """Restricts access to authenticated users only."""
    