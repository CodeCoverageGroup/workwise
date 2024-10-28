from django.db import models

class Job(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Ensure title is always returned as a string
        return str(self.title) if self.title else "No Title"
