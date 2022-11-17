from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=40, verbose_name='Título')
    img = models.ImageField(upload_to='gallery', verbose_name='Imagen')
    wide = models.BooleanField(verbose_name='Imagen ancha', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')

    class Meta():
        verbose_name = 'Galería'
        verbose_name_plural ='Galería'

    def __str__(self):
        return self.title
