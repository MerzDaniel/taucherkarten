from django.db import models

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

    def __str__(self):
        return self.name

class Divespot(models.Model):
    name = models.CharField(max_length=100)
    lake = models.ForeignKey(
        Lake, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
