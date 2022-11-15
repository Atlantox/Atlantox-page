from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('briefcase/', views.briefcase, name='Briefcase')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)