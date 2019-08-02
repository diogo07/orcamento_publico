from django.shortcuts import render

def get_index(request):
    return render(request, 'index.html')

def get_orcamento(request):
    return render(request, 'orcamento.html')

def get_receitas_orcamentarias(request):
    return render(request, 'receitas_orcamentarias.html')

def get_municipios(request):
    return render(request, 'municipios.html')