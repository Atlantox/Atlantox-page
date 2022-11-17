from django.contrib import admin
from . import models

class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(models.Gallery, GalleryAdmin)

