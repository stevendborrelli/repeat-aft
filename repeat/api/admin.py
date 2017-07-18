from django.contrib import admin
from django.db import models as django_models
from . import models

# Register your models here.
for _, value in models.__dict__.items():
    try:
        if issubclass(value, django_models.Model):
            admin.site.register(value)
    except TypeError:
        pass
# admin.site.register()
