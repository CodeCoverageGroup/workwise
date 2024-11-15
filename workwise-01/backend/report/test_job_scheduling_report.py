# reports/tests/test_job_scheduling_report.py
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from jobs.models import Job, JobAssignment
from accounts.models import User  # Assuming the Employee model is in accounts

class EmployeeJobSchedulingReportTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test data for employees, jobs, and job assignments
        cls.employee1 = User.objects.create_user(username="employee1", password="password1")
        cls.employee2 = User.objects.create_user(username="employee2", password="password2")

        # Create test jobs
        cls.job1 = Job.objects.create(
            title="Job 1",
            description="First test job",
            deadline=timezone.now() + timezone.timedelta(days=5),
            is_complete=False
        )
        cls.job2 = Job.objects.create(
            title="Job 2",
            description="Second test job",
            deadline=timezone.now() + timezone.timedelta(days=10),
            is_complete=False
        )

        # Assign jobs to employees
        cls.assignment1 = JobAssignment.objects.create(
            job=cls.job1,
            employee=cls.employee1,
            assigned_date=timezone.now(),
            completion_date=None
        )
        cls.assignment2 = JobAssignment.objects.create(
            job=cls.job2,
            employee=cls.employee2,
            assigned_date=timezone.now(),
            completion_date=None
        )

    def test_job_scheduling_report_data(self):
        # Send GET request to job scheduling report endpoint
        response = self.client.get(reverse('job_scheduling_report'))  # Replace with actual URL name
        self.assertEqual(response.status_code, 200)

        # Parse the response data (assuming JSON format)
        data = response.json()

        # Check if the response contains job assignments for employees
        self.assertIn('employee_jobs', data)
        self.assertEqual(len(data['employee_jobs']), 2)  # Should include 2 employees

        # Validate details for the first employee job
        employee1_jobs = next((item for item in data['employee_jobs'] if item['employee'] == self.employee1.username), None)
        self.assertIsNotNone(employee1_jobs)
        self.assertEqual(len(employee1_jobs['jobs']), 1)
        self.assertEqual(employee1_jobs['jobs'][0]['title'], "Job 1")
        self.assertEqual(employee1_jobs['jobs'][0]['description'], "First test job")
        self.assertFalse(employee1_jobs['jobs'][0]['is_complete'])

        # Validate details for the second employee job
        employee2_jobs = next((item for item in data['employee_jobs'] if item['employee'] == self.employee2.username), None)
        self.assertIsNotNone(employee2_jobs)
        self.assertEqual(len(employee2_jobs['jobs']), 1)
        self.assertEqual(employee2_jobs['jobs'][0]['title'], "Job 2")
        self.assertEqual(employee2_jobs['jobs'][0]['description'], "Second test job")
        self.assertFalse(employee2_jobs['jobs'][0]['is_complete'])
