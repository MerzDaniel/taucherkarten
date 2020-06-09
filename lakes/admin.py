from django.contrib import admin
from lakes import models

# Register your models here.
admin.site.register(models.Country)
admin.site.register(models.State)
admin.site.register(models.District)
admin.site.register(models.Lake)
admin.site.register(models.Divespot)
admin.site.register(models.Divemap)
