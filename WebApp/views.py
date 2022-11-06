from django.shortcuts import render

def home(request):
    ctx = {}
    return render(request, 'WebApp/home.html', ctx)

def contact(request):
    return render(request, 'WebApp/contact.html', dict())
