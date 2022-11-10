from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('projects/', views.projects, name='Projects'),
    path('project/<int:id>', views.projects, name='Project'),
    path('category/<int:id>', views.projects, name='Category'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)