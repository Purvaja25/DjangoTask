from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='clients_created_by',
    )
    updated_by = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='clients_updated_by',
    )



class Project(models.Model):
    project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects", null=True, blank=True)
    users = models.ManyToManyField(User, related_name="assigned_projects", blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='projects_created_by',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='projects_updated_by',
    )