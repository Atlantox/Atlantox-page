from django.shortcuts import render
from . import models

def gallery(request):
    wide_images = models.Gallery.objects.filter(wide=True)
    tall_images = models.Gallery.objects.filter(wide=False)
    ctx = {
        'wide_images': wide_images,
        'tall_images': tall_images
        }

    return render(request, 'GalleryApp/gallery.html', ctx)
