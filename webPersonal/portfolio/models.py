from django.db import models
from django.utils import timezone
class Proyect(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    icon = models.ImageField(verbose_name="Icono", upload_to="projects", blank=True)
    urlProyecto = models.CharField(max_length=200, verbose_name="Git", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title
class ProjectImage(models.Model):
    project = models.ForeignKey(Proyect, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Imagen adicional", upload_to="projects")
    created = models.DateTimeField(default=timezone.now)
# Automatically set the field to now when the object is created
    updated = models.DateTimeField(default=timezone.now)  # Automatically set the field to now every time the object is saved

    class Meta:
        verbose_name = 'Imagen de Proyecto'
        verbose_name_plural = 'Imágenes de Proyecto'

    def __str__(self):
        return f"Imagen para {self.project.title}"
