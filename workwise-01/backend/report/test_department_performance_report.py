# reports/tests/test_department_performance_report.py
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from departments.models import Department, Project
from accounts.models import User

class DepartmentalPerformanceReportTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up departments and employees
        cls.department1 = Department.objects.create(name="Research and Development")
        cls.department2 = Department.objects.create(name="Marketing")

        # Create test employees
        cls.employee1 = User.objects.create_user(username="employee1", password="password1")
        cls.employee2 = User.objects.create_user(username="employee2", password="password2")

        # Assign employees to departments (assuming a ManyToMany relationship)
        cls.department1.employees.add(cls.employee1)
        cls.department2.employees.add(cls.employee2)

        # Create projects for each department
        cls.project1 = Project.objects.create(
            title="Project Alpha",
            department=cls.department1,
            deadline=timezone.now() + timezone.timedelta(days=10),
            actual_completion_date=None,  # Ongoing project
            completion_status="Ongoing"
        )
        cls.project2 = Project.objects.create(
            title="Project Beta",
            department=cls.department1,
            deadline=timezone.now() - timezone.timedelta(days=5),  # Overdue
            actual_completion_date=None,
            completion_status="Delayed"
        )
        cls.project3 = Project.objects.create(
            title="Project Gamma",
            department=cls.department2,
            deadline=timezone.now() - timezone.timedelta(days=10),
            actual_completion_date=timezone.now() - timezone.timedelta(days=2),
            completion_status="Completed"
        )

    def test_department_performance_report_data(self):
        # Send GET request to the department performance report endpoint
        response = self.client.get(reverse('department_performance_report'))  # Replace with actual URL name
        self.assertEqual(response.status_code, 200)

        # Parse the response data (assuming JSON format)
        data = response.json()

        # Check if the response contains performance data for departments
        self.assertIn('departments', data)
        self.assertEqual(len(data['departments']), 2)  # Should include 2 departments

        # Validate data for the first department
        department1_data = next((dept for dept in data['departments'] if dept['name'] == "Research and Development"), None)
        self.assertIsNotNone(department1_data)
        self.assertEqual(department1_data['total_projects'], 2)
        self.assertEqual(department1_data['completed_projects'], 0)
        self.assertEqual(department1_data['delayed_projects'], 1)
        self.assertEqual(department1_data['ongoing_projects'], 1)

        # Validate data for the second department
        department2_data = next((dept for dept in data['departments'] if dept['name'] == "Marketing"), None)
        self.assertIsNotNone(department2_data)
        self.assertEqual(department2_data['total_projects'], 1)
        self.assertEqual(department2_data['completed_projects'], 1)
        self.assertEqual(department2_data['delayed_projects'], 0)
        self.assertEqual(department2_data['ongoing_projects'], 0)
