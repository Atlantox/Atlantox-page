from django.shortcuts import render
from . import models

def briefcase(request):
    briefcases = models.Briefcase.objects.all()
    helf_briefcase = int(len(briefcases) / 2)

    ctx = {
        'briefcases1': briefcases[0:helf_briefcase],
        'briefcases2' : briefcases[helf_briefcase:len(briefcases)]
        }
    return render(request, 'BriefcaseApp/briefcase.html', ctx)
