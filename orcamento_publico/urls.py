"""orcamento_publico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from orcamento_publico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index),
    url(r'^api/', include(('api.urls', 'api'), namespace='api')),
    url(r'^orcamento', views.get_orcamento),
    url(r'^receitas', views.get_receitas),
    url(r'^despesas', views.get_despesas),
    url(r'^municipios', views.get_municipios),
]
