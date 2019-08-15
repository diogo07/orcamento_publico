from django.urls import path
from api import views
app_name = 'api'
urlpatterns = [

    # BUSCA DE MUNICIPIO POR CODIGO E POR NOME
    path('municipio/<int:codigo_municipio>/', views.municipio_by_codigo),
    path('municipio/<slug:nome_municipio>/', views.municipio_by_nome),

    # DESPESAS DE UM MUNICÍPIO POR FUNÇÃO OU CLASSIFICAÇÃO EM UM DETERMINADO ANO
    path('despesa/classificacao/municipio/<int:codigo_municipio>/ano/<int:ano>', views.despesa_por_classificacao_municipio_e_ano),
    path('despesa/funcao/municipio/<int:codigo_municipio>/ano/<int:ano>',
         views.despesa_por_funcao_municipio_e_ano),

    # DESPESAS TOTAIS POR ANO DE UM MUNICIPIO
    path('despesa/municipio/<int:codigo_municipio>', views.despesa_por_municipio),


    # RECEITAS DE UM MUNICÍPIO POR FUNÇÃO OU CLASSIFICAÇÃO EM UM DETERMINADO ANO
    path('receita/classificacao/municipio/<int:codigo_municipio>/ano/<int:ano>', views.receita_por_classificacao_municipio_e_ano),
    path('receita/funcao/municipio/<int:codigo_municipio>/ano/<int:ano>',
         views.receita_por_funcao_municipio_e_ano),

    # DESPESAS TOTAIS POR ANO DE UM MUNICIPIO
    path('receita/municipio/<int:codigo_municipio>', views.receita_por_municipio),


]
