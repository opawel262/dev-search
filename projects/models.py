from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    source_code = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"PROJECT TITLE - '{self.title}'"
    
 
class Review(models.model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"REVIEW OF '{self.project.title}' BY '{self.user_name}'"

    def __str__(self):
        return f"PROJECT TITLE - '{self.title}'"
