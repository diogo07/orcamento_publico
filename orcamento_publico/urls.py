from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from orcamento_publico import views, settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index),
    path('api/', include('api.urls'),),
    path('orcamento', views.get_orcamento),
    path('receitas', views.get_receitas),
    path('despesas', views.get_despesas),
    path('municipios', views.get_municipios),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
