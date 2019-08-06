from django.shortcuts import render

def get_index(request):
    return render(request, 'index.html')

def get_orcamento(request):
    return render(request, 'orcamento.html')

def get_receitas(request):
    return render(request, 'receitas_orcamentarias.html')

def get_despesas(request):
    return render(request, 'despesas_orcamentarias.html')

def get_municipios(request):
    return render(request, 'municipios.html')