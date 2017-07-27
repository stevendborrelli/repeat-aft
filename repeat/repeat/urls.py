"""repeat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf import urls
from django.contrib import admin

urlpatterns = [
    urls.url(r'^admin/', admin.site.urls),
    urls.url(r'^api/v0/', urls.include("api.urls")),

    # User registration
    urls.url(r"^accounts/", urls.include("registration.backends.simple.urls")),
]
