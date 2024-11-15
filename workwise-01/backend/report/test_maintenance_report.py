# reports/tests/test_maintenance_report.py
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from machines.models import Machine, MaintenanceLog
from accounts.models import User  # Assuming User model is in accounts

class MachineMaintenanceReportTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up user and machine data
        cls.maintenance_personnel = User.objects.create_user(
            username="maintenance_user", password="password"
        )
        cls.machine = Machine.objects.create(
            name="Test Machine",
            description="Machine for testing maintenance report",
            last_maintenance_date=timezone.now()
        )
        # Create maintenance logs
        cls.log1 = MaintenanceLog.objects.create(
            machine=cls.machine,
            personnel=cls.maintenance_personnel,
            date=timezone.now() - timezone.timedelta(days=30),
            description="Routine check-up"
        )
        cls.log2 = MaintenanceLog.objects.create(
            machine=cls.machine,
            personnel=cls.maintenance_personnel,
            date=timezone.now() - timezone.timedelta(days=60),
            description="Repair"
        )

    def test_maintenance_report_data(self):
        # Test the report generation endpoint
        response = self.client.get(reverse('maintenance_report'))  # Replace with actual URL name
        self.assertEqual(response.status_code, 200)

        # Parse the response data (assuming JSON format)
        data = response.json()

        # Check the returned data contains correct machine information
        self.assertIn('machine_name', data)
        self.assertEqual(data['machine_name'], self.machine.name)

        # Check that maintenance logs are returned and include expected fields
        self.assertIn('maintenance_logs', data)
        self.assertEqual(len(data['maintenance_logs']), 2)
        
        # Verify specific log data
        self.assertEqual(data['maintenance_logs'][0]['description'], "Routine check-up")
        self.assertEqual(data['maintenance_logs'][1]['description'], "Repair")
