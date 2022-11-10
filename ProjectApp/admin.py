from django.contrib import admin
from ProjectApp import models

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)

admin.site.register(models.Category)
admin.site.register(models.Project, ProjectAdmin)