from django.db import models
from django.template.defaultfilters import slugify
import autoslug

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Lake(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE
    )
    slug = autoslug.AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class Divespot(models.Model):
    name = models.CharField(max_length=100)
    lake = models.ForeignKey(
        Lake, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Divemap(models.Model):
    image = models.ImageField(height_field='height', width_field='width')
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    divespot = models.ForeignKey(
        Divespot, on_delete=models.CASCADE
    )

