from departments.models import Department, Project
from jobs.models import Job
from machines.models import Machine, MaintenanceLog

class DepartmentPerformanceReport:
    @staticmethod
    def get_performance_data():
        performance_data = []
        departments = Department.objects.all()
        
        for department in departments:
            project_count = department.projects.count()
            jobs = Job.objects.filter(project__department=department)
            job_counts_by_priority = {
                'low': jobs.filter(priority=1).count(),
                'medium': jobs.filter(priority=2).count(),
                'high': jobs.filter(priority=3).count()
            }
            maintenance_ticket_count = MaintenanceLog.objects.filter(machine__department=department).count()

            performance_data.append({
                'department': department.name,
                'project_count': project_count,
                'job_counts_by_priority': job_counts_by_priority,
                'maintenance_ticket_count': maintenance_ticket_count
            })
        
        return performance_data
