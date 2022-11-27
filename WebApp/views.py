from django.shortcuts import render
from ProjectApp.models import Project
from django.forms.models import model_to_dict

def home(request):
    projects = Project.objects.all().order_by('-id')[:2]
    buffer = []

    for project in projects:
        project.content = text_resumer(project.content)
        buffer.append(model_to_dict(project))

    buffer[0]['first'] = True
    ctx = {'projects': buffer}
    return render(request, 'WebApp/home.html', ctx)

def contact(request):
    return render(request, 'WebApp/contact.html', dict())

def text_resumer(text):
    return text[0:100] + '...'