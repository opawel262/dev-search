from django.shortcuts import render
from .models import Project
from uuid import UUID
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

    
def single_project(request, pk: UUID):
    project = Project.objects.get(id=pk)
    data = {'project': project}
    return render(request, 'projects/single_project.html', data)
    

def create_project(request):
    context = {
        
    }
    return render(request, 'projects/create_project.html')
    