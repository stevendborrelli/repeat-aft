"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


def list_url(name, view, plural=None):
    """ Make a url of the form /resources for a given resource """
    return url(r'^{}$'.format(plural or name + "s"),
               view,
               name="{}_list".format(name))


def crud_url(name, view, plural=None):
    """ Make a url of the form /resources/pk for a given resource """
    return url(r'^{}/(?P<pk>[^/]+)$'.format(plural or name + "s"),
               view,
               name="{}_crud".format(name))


urlpatterns = [
    # url(r'^$', views.schema_view, name="analysis_schema"),

    # Domains
    list_url("domain", views.DomainList.as_view()),
    crud_url("domain", views.DomainCRUD.as_view()),

    # Papers
    list_url("paper", views.PaperList.as_view()),
    crud_url("paper", views.PaperCRUD.as_view()),

    # Variables
    list_url("variable", views.VariableList.as_view()),
    crud_url("variable", views.VariableCRUD.as_view()),

    # Binaries
    list_url(
        "binary", views.BinaryList.as_view(), plural="binaries"),
    crud_url(
        "binary", views.BinaryCRUD.as_view(), plural="binaries"),

    # Values
    list_url("value", views.ValueList.as_view()),
    crud_url("value", views.ValueCRUD.as_view()),

    # List the variables of a domain
    url(r"^lists/(?P<pk>[^/]+)$",
        views.VariablesByDomain.as_view(),
        name="variable_lists")
]

urlpatterns = format_suffix_patterns(urlpatterns)
