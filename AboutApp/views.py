from django.shortcuts import render
from . import models

def about(request):
    pleasures = models.Pleasure.objects.all()
    ctx = {'pleasures': pleasures}
    return render(request, 'AboutApp/about.html', ctx)
