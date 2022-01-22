from django.db import models

# My models here.

class Trailers(models.Model):
    title = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Trailer"
        verbose_name_plural = "Trailers"