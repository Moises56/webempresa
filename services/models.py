from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.TextField(verbose_name='Sub-Titulo')
    content = models.CharField(max_length=200, verbose_name='Contenido')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created_at']

    def __str__(self):
        return self.title