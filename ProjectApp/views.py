from django.shortcuts import render
from . import models

def projects(request):
    projects = models.Project.objects.all().order_by('-id')
    categories = models.Category.objects.all()

    for project in projects:
        project.content = text_resumer(project.content)

    ctx = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'ProjectApp/projects.html', ctx)

def project(request, id):
    ctx = {}
    return render(request, 'ProjectApp/category.html', ctx)

def category(request, id):
    ctx = {}
    return render(request, 'ProjectApp/project.html', ctx)


def text_resumer(text):
    return text[0:100] + '...'