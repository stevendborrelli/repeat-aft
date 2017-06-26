from rest_framework import serializers
import functools
from . import models


def export_fields(model, fields="__all__"):
    """ Create a ModelSerializer that exports certain fields """
    meta = type("Meta", (), {"model": model, "fields": fields})
    return type(model.__name__ + "Serializer", (serializers.ModelSerializer, ),
                {"Meta": meta})

# Create a ModelSerializer that exports only the name field
name_only = functools.partial(export_fields, fields=["name"])

# Serializers that export every field
Domain = export_fields(models.Domain)
Paper = export_fields(models.Paper)  # TODO: export the File field?
Variable = export_fields(models.Variable)
Binary = export_fields(models.Binary)
OneFromMany = export_fields(models.OneFromMany)
ManyFromMany = export_fields(models.ManyFromMany)
Value = export_fields(models.Value)

# Other serializers
VariableName = name_only(models.Variable)
