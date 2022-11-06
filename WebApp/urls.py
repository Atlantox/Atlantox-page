from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)