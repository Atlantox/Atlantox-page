from django.shortcuts import render
from . import models

def projects(request):
    projects = get_projects().order_by('-id')
    categories = get_categories()

    for project in projects:
        project.content = text_resumer(project.content)

    ctx = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'ProjectApp/projects.html', ctx)

def project(request, id):
    project = models.Project.objects.get(id=id)
    categories = get_categories()
    ctx = {
        'project': project,
        'categories': categories
    }
    return render(request, 'ProjectApp/project.html', ctx)

def category(request, id):
    category = models.Category.objects.get(id=id)
    projects = models.Project.objects.filter(category=category)

    for project in projects:
        project.content = text_resumer(project.content)

    ctx = {
        'category': category,
        'projects': projects,
        'categories': get_categories()
        }
    return render(request, 'ProjectApp/category.html', ctx)


def text_resumer(text):
    return text[0:100] + '...'

def get_categories():
    return models.Category.objects.all()

def get_projects():
    return models.Project.objects.all()