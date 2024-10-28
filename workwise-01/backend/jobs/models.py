from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title