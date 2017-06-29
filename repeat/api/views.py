from django.shortcuts import render
from django.http import JsonResponse
import django.shortcuts

# API schema views
from rest_framework import decorators
from rest_framework import renderers
from rest_framework import response
# from rest_framework import schema
# Other views
from rest_framework import generics
from rest_framework import permissions
from rest_framework import views
from . import models
from . import serializers

# API Schema views
# TODO: Automatically export/encode as a simple .json schema file
# http://core-api.github.io/python-client/api-guide/codecs/

# @decorators.api_view()
# @decorators.renderer_classes([renderers.CoreJSONRenderer])
# def schema_view(request):
#     """ View the API schema """
#     schema = schemas.SchemaGenerator(title="Analysis API").get_schema(request)
#     return response.Response(schema)


def list_and_crud(model, serializer, queryset=None):
    """
    Create a ListCreateAPIView and RetrieveUpdateDestroyAPIView corresponsing
    to a given model/serializer pair.

    It's like writing the following code manually (when called on model
    ``Foo``)::

        class FooList(generics.ListCreateAPIView):
            queryset = models.Foo.objects.all()
            serializer_class = serializers.FooSerializer


        class FooRUD(generics.RetrieveUpdateDestroyAPIView):
            queryset = models.Foo.objects.all()
            serializer_class = serializers.FooSerializer
    """
    queryset = model.objects.all() if queryset is None else queryset
    lst = type(model.__name__ + "List", (generics.ListCreateAPIView, ), {})
    rud = type(model.__name__ + "CRUD",
               (generics.RetrieveUpdateDestroyAPIView, ), {})
    lst.queryset = queryset
    lst.serializer_class = serializer
    lst.permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    rud.queryset = queryset
    rud.serializer_class = serializer
    rud.permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    return (lst, rud)


DomainList, DomainCRUD = list_and_crud(models.Domain, serializers.Domain)

PaperList, PaperCRUD = list_and_crud(models.Paper, serializers.Paper)

VariableList, VariableCRUD = list_and_crud(models.Variable,
                                           serializers.Variable)

BinaryList, BinaryCRUD = list_and_crud(models.Binary, serializers.Binary)

ValueList, ValueCRUD = list_and_crud(models.Value, serializers.Value)


class VariablesByDomain(views.APIView):
    """ List the variables belonging to a certain domain """

    def get(self, request, pk=None):
        # Ensure such a domain exists, or raise a 404
        _ = django.shortcuts.get_object_or_404(models.Domain, pk=pk)
        # Filter for Variables that have this domain in their .domains field
        # TODO: use values(*fields) or only() to only fetch the names
        return response.Response(
            serializers.VariableName(
                models.Variable.objects.filter(domains__name__exact=pk),
                many=True).data)


class Extract(views.APIView):
    """
    Extract variables from a Paper. A single variable can be specified using
    its primary key, or all variables will be extracted.
    """

    def get(self, request, paperpk=None):
        if pk is not None:
            _ = django.shortcuts.get_object_or_404(models.Variable, pk=pk)
