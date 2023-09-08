from django.shortcuts import render, redirect
from .models import Project
from uuid import UUID
from .forms import ProjectForm
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
    
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')
        
    context = {
        'form': form
    }
    return render(request, 'projects/create_project.html', context)
    

def update_project(request, pk: UUID):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')
    context = {
        'form': form
    }
    return render(request, 'projects/update_project.html', context)


def delete_project(request, pk: UUID):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects:projects')
    context = {
        'form': form
    }
    return render(request, 'projects/delete_project.html', context)
    
    
    
    
    