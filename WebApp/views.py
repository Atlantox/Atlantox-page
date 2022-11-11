from django.shortcuts import render
from ProjectApp.models import Project

def home(request):
    projects = Project.objects.all().order_by('-id')[:2]

    for project in projects:
        project.content = text_resumer(project.content)

    ctx = {'projects': projects}
    return render(request, 'WebApp/home.html', ctx)

def contact(request):
    return render(request, 'WebApp/contact.html', dict())

def text_resumer(text):
    return text[0:100] + '...'