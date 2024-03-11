from django.contrib import admin

from WebBulder import models

# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.SpeshalCar)
admin.site.register(models.Service)
admin.site.register(models.BuildMaterials)
admin.site.register(models.Costumer)