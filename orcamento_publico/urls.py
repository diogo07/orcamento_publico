from django.contrib import admin
from django.urls import path, include

from orcamento_publico import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.get_index),
    path('api/', include('api.urls'),),
    path('orcamento', views.get_orcamento),
    path('receitas', views.get_receitas),
    path('despesas', views.get_despesas),
    path('municipios', views.get_municipios),
]
