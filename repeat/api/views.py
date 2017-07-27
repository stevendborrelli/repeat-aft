import django.shortcuts

# API schema views
# from rest_framework import decorators
# from rest_framework import renderers
from rest_framework import response
# from rest_framework import schema
# Other views
from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import views
from api.analysis import analysis
from api import models
from api import serializers

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
            ...


        class FooRUD(generics.RetrieveUpdateDestroyAPIView):
            queryset = models.Foo.objects.all()
            serializer_class = serializers.FooSerializer
            ...
    """
    queryset = model.objects.all() if queryset is None else queryset
    lst = type(model.__name__ + "List", (generics.ListCreateAPIView, ), {})
    rud = type(model.__name__ + "CRUD",
               (generics.RetrieveUpdateDestroyAPIView, ), {})

    for cls in (lst, rud):
        cls.queryset = queryset
        cls.serializer_class = serializer
        cls.authentication_classes = (authentication.BasicAuthentication, )
        cls.permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    return (lst, rud)


DomainList, DomainCRUD = list_and_crud(models.Domain, serializers.Domain)

CategoryList, CategoryCRUD = list_and_crud(models.Category, serializers.Category)

PaperList, PaperCRUD = list_and_crud(models.Paper, serializers.Paper)

VariableList, VariableCRUD = list_and_crud(models.Variable,
                                           serializers.Variable)

BinaryList, BinaryCRUD = list_and_crud(models.Binary, serializers.Binary)

ValueList, ValueCRUD = list_and_crud(models.Value, serializers.Value)


class VariablesByDomain(views.APIView):
    """ List the variables belonging to a certain domain """

    def get(self, request, pk=None):
        # Ensure such a domain exists, or raise a 404
        django.shortcuts.get_object_or_404(models.Domain, pk=pk)
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

    TODO: multiple
    """
    @staticmethod
    def extract_all(text):
        """ Extract Values with all available plugins """
        all_responses = dict()
        for variable in models.Variable.objects.all():
            try:
                all_responses[variable.pk] = analysis.extract(text,
                                                              variable.pk)
            except ImportError:
                continue
        return all_responses

    def get(self, request, paperpk=None, varpk=None):
        if varpk is not None:
            _ = django.shortcuts.get_object_or_404(models.Variable, pk=varpk)
        paper = django.shortcuts.get_object_or_404(models.Paper, pk=paperpk)
        text, _ = paper.get_text()

        # If one is specified, return that one
        if varpk is not None:
            return response.Response(
                data={"value": analysis.extract(text, varpk)})

        # Extract all variables and return them
        return response.Response(data=self.extract_all(text))
