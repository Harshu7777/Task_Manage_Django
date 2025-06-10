from django.db import models
from django.contrib.auth.models import User

# Create your models here.  due_date, priority, status
class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Med', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.BooleanField(default=False)
    file = models.FileField(upload_to='task_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
