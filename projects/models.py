from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    source_link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    