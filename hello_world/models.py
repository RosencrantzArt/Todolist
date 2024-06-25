from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)  # Optional field for additional information
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Adjust as needed
    status = models.CharField(max_length=20, choices=[('P', 'Pending'), ('C', 'Completed')], default='P')


 