from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')

    class Meta():
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    img = models.ImageField(upload_to='projects/', verbose_name='Imagen')
    link = models.TextField(verbose_name='Enlace')
    content = models.TextField(verbose_name='Contenido')
    category = models.ManyToManyField(Category, verbose_name='Categoría')
    created = models.DateTimeField(auto_now=True, verbose_name='Creado en')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado en')

    class Meta():
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.name
