from django.db import models

# My models here.

# Sector models

class Sector(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    excerpt = models.TextField(blank=True)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

# Category model

class Category(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# Trailers model.

class Trailers(models.Model):

    def __str__(self):
        return self.name

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True)
    excerpt = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Trailer"
        verbose_name_plural = "Trailers"



