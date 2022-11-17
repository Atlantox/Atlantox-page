from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('gallery/', views.gallery, name='Gallery')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)