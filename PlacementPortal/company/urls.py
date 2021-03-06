"""PlacementPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'shortlist/$', views.shortlist, name = 'shortlist'),
    url(r'confirmation/(?P<pk>[0-9]+)$', views.confirmation, name = 'confirmation'),
    url(r'new_jaf/$', views.new_jaf, name = 'new_jaf'),
    url(r'jaf/(?P<pk>[0-9]+)$', views.view_students, name = 'view_students'),
    url(r'logout/$', views.logout, name = 'logout'),
    url(r'$', views.home, name = 'home'),
]