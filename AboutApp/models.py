from django.db import models

class Pleasure(models.Model):
    name = models.CharField(max_length=45, verbose_name='Título')
    img = models.ImageField(upload_to='about', verbose_name='Imagen')

    class Meta():
        verbose_name = 'Gusto'
        verbose_name_plural = 'Gustos'

    def __str__(self):
        return self.name
