from . import models

# Serializers that export every field
Domain = models.get_serializer(models.Domain)
Category = models.get_serializer(models.Category)
Paper = models.get_serializer(models.Paper)
Variable = models.get_serializer(models.Variable)
Binary = models.get_serializer(models.Binary)
OneFromMany = models.get_serializer(models.OneFromMany)
ManyFromMany = models.get_serializer(models.ManyFromMany)
Value = models.get_serializer(models.Value)

# Other serializers
VariableName = models.get_serializer(models.Variable, fields=("name",))
