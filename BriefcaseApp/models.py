from django.db import models

class Briefcase(models.Model):
    title = models.CharField(max_length=55, verbose_name='Título')
    img = models.ImageField(upload_to='briefcase/', verbose_name='Imagen')

    class Meta():
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'

    def __str__(self):
        return self.title
