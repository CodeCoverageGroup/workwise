# pylint: disable=no-member

from django.db import models
from django.contrib.auth.models import User

class Machine(models.Model):
    name = models.CharField(max_length=100)  # Name of the machine
    model_number = models.CharField(max_length=100)  # Model number of the machine
    location = models.CharField(max_length=100)  # Location where the machine is placed
    status = models.CharField(max_length=50, choices=[('operational', 'Operational'), ('maintenance', 'Maintenance')])  # Status of the machine
    last_maintenance_date = models.DateField(null=True, blank=True)  # Last maintenance date, optional

    def __str__(self):
        # Ensure the __str__ method returns a string value, which represents the machine
        return f"Machine: {self.name} (Model: {self.model_number})"

class MaintenanceTicket(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='tickets')
    issue_description = models.TextField()  # This should store text, which is a string
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    # Safely handle issue_description even if it's None or not a valid string
    if isinstance(self.issue_description, str):
        # If issue_description is a valid string, slice and return the first 20 characters
        return f"Ticket for {self.machine.name}: {self.issue_description[:20]}... (Status: {self.status})"
    else:
        # If issue_description is None or not a string, return a default string
        return f"Ticket for {self.machine.name}: No description provided (Status: {self.status})"
