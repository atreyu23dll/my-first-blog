from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    crear_fecha = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
