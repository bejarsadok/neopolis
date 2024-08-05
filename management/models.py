from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
import uuid


class Project(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='member')

    def __str__(self):
        return self.name


class Task(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    assiged_to = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
