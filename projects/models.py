from django.db import models
import uuid
# Create your models here.


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"TAG NAME - '{self.name}'"


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    demo_link = models.URLField(max_length=200, null=True, blank=True)
    source_code = models.URLField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(null=True, blank=True, default="default.jpg")
    
    def __str__(self):
        return f"PROJECT TITLE - '{self.title}'"
    
 
class Review(models.Model):
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

