from django.contrib import admin
from .models import Project, Tag, Review

# Register your models here.
admin.site.register(Project, Tag, Review)