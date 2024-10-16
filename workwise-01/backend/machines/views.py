# pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Machine, MaintenanceTicket
from .serializers import MachineSerializer, MaintenanceTicketSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class MaintenanceTicketViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTicket.objects.all()
    serializer_class = MaintenanceTicketSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
