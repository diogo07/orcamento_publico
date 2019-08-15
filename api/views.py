from api.models import Municipio, Receita, Despesa
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from api.serializers import MunicipioSerializer, ReceitaSerializer
from django.views.generic.edit import UpdateView
import re
# BUSCA O MUNICIPIO PELO CÓDIGO
def municipio_by_codigo(request, codigo_municipio):
    try:
        municipio = Municipio.objects.filter(codigo=codigo_municipio)
    except Municipio.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MunicipioSerializer(municipio, many=True)
        return JsonResponse(serializer.data, safe=False)

# BUSCA O MUNICIPIO PELO NOME
def municipio_by_nome(request, nome_municipio):
    try:
        nome_acentuado = tratar_caracteres_especiais(nome_municipio)
        print(nome_acentuado)
        nome_tratado = nome_acentuado.replace('_', ' ')
        municipio = Municipio.objects.filter(nome__icontains=nome_tratado)
    except Municipio.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MunicipioSerializer(municipio, many=True)
        return JsonResponse(serializer.data, safe=False)


# BUSCA AS DESPESAS DE UM MUNICIPIO POR CLASSIFICAÇÃO E ANO
def despesa_por_classificacao_municipio_e_ano(request, codigo_municipio, ano):
    try:
        despesas = Despesa.objects.filter(municipio_codigo=codigo_municipio, ano=ano).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'classificacao_despesa_codigo__tipo', 'ano').annotate(valor_total = Sum('valor')).order_by('-valor_total')

        context = []
        dados = []
        for despesa in despesas:
            dados.append(
                {
                    'classificacao': despesa['classificacao_despesa_codigo__tipo'],
                    'valor': despesa['valor_total']
                }
            )

        context.append(
            {
                'municipio': despesas[0]['municipio_codigo__nome'],
                'uf': despesas[0]['municipio_codigo__uf'],
                'regiao': despesas[0]['municipio_codigo__regiao'],
                'ano': despesas[0]['ano'],
                'despesas': dados

            }
        )

    except Despesa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(context, safe=False)

# BUSCA AS DESPESAS DE UM MUNICIPIO POR FUNÇÃO E ANO
def despesa_por_funcao_municipio_e_ano(request, codigo_municipio, ano):
    try:
        despesas = Despesa.objects.filter(municipio_codigo=codigo_municipio, ano=ano).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'classificacao_despesa_codigo__tipo', 'funcao_despesa_codigo__tipo', 'ano').annotate(valor_total = Sum('valor')).order_by('-valor_total')

        context = []
        dados = []
        for despesa in despesas:
            dados.append(
                {
                    'classificacao' : despesa['classificacao_despesa_codigo__tipo'],
                    'funcao' : despesa['funcao_despesa_codigo__tipo'],
                    'valor' : despesa['valor_total']
                }
            )

        context.append(
            {
                'municipio': despesas[0]['municipio_codigo__nome'],
                'uf': despesas[0]['municipio_codigo__uf'],
                'regiao': despesas[0]['municipio_codigo__regiao'],
                'ano': despesas[0]['ano'],
                'despesas': dados

            }
        )

    except Despesa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(context, safe=False)


# BUSCA AS DESPESAS DE UM MUNICIPIO, E AGRUPA O VALOR TOTAL POR ANO
def despesa_por_municipio(request, codigo_municipio):
    try:
        despesas = Despesa.objects.filter(municipio_codigo=codigo_municipio).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'ano').annotate(valor_total = Sum('valor')).order_by('ano')

        context = []
        dados = []

        print(despesas[0]['ano'])
        for despesa in despesas:
            dados.append(
                {
                    despesa['ano']: despesa['valor_total']
                }
            )

        context.append(
            {
                'municipio': despesas[0]['municipio_codigo__nome'],
                'uf': despesas[0]['municipio_codigo__uf'],
                'regiao': despesas[0]['municipio_codigo__regiao'],
                'despesas': dados

            }
        )

    except Despesa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(context, safe=False)


# BUSCA AS RECEITAS DE UM MUNICIPIO, E AGRUPA O VALOR TOTAL POR ANO
def receita_por_municipio(request, codigo_municipio):
    try:
        receitas = Receita.objects.filter(municipio_codigo=codigo_municipio).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'ano').annotate(valor_total = Sum('valor')).order_by('ano')

        context = []
        dados = []
        for receita in receitas:
            dados.append(
                {
                    receita['ano']: receita['valor_total']
                }
            )

        context.append(
            {
                'municipio': receitas[0]['municipio_codigo__nome'],
                'uf': receitas[0]['municipio_codigo__uf'],
                'regiao': receitas[0]['municipio_codigo__regiao'],
                'receitas': dados

            }
        )

    except Receita.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(context, safe=False)

# BUSCA AS RECEITAS DE UM MUNICIPIO POR CLASSIFICAÇÃO E ANO
def receita_por_classificacao_municipio_e_ano(request, codigo_municipio, ano):
    try:
        receitas = Receita.objects.filter(municipio_codigo=codigo_municipio, ano=ano).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'classificacao_receita_codigo__tipo', 'ano').annotate(valor_total = Sum('valor')).order_by('-valor_total')

        context = []
        dados = []
        for receita in receitas:
            dados.append(
                {
                    'classificacao': receita['classificacao_receita_codigo__tipo'],
                    'valor': receita['valor_total']
                }
            )

        context.append(
            {
                'municipio': receitas[0]['municipio_codigo__nome'],
                'uf': receitas[0]['municipio_codigo__uf'],
                'regiao': receitas[0]['municipio_codigo__regiao'],
                'ano': receitas[0]['ano'],
                'receitas': dados

            }
        )

    except Receita.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(context, safe=False)

# BUSCA AS RECEITAS DE UM MUNICIPIO POR FUNÇÃO E ANO
def receita_por_funcao_municipio_e_ano(request, codigo_municipio, ano):
    try:
        receitas = Receita.objects.filter(municipio_codigo=codigo_municipio, ano=ano).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'funcao_receita_codigo__tipo', 'ano').annotate(valor_total = Sum('valor')).order_by('-valor_total')

        context = []
        dados = []
        for receita in receitas:
            dados.append(
                {
                    'funcao' : receita['funcao_receita_codigo__tipo'],
                    'valor': receita['valor_total']
                }
            )

        context.append(
            {
                'municipio': receitas[0]['municipio_codigo__nome'],
                'uf': receitas[0]['municipio_codigo__uf'],
                'regiao': receitas[0]['municipio_codigo__regiao'],
                'ano': receitas[0]['ano'],
                'despesas': dados

            }
        )

    except Receita.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return JsonResponse(context, safe=False)


def tratar_caracteres_especiais(palavra):
    palavra = palavra.lower()
    palavra = re.sub(r'__tila__', 'ã', palavra)
    palavra = re.sub(r'__tilo__', 'õ', palavra)
    palavra = re.sub(r'__circunflexoa__', 'â', palavra)
    palavra = re.sub(r'__circunflexoe__', 'ê', palavra)
    palavra = re.sub(r'__circunflexoo__', 'ô', palavra)
    palavra = re.sub(r'__agudoa__', 'á', palavra)
    palavra = re.sub(r'__agudoe__', 'é', palavra)
    palavra = re.sub(r'__agudoi__', 'í', palavra)
    palavra = re.sub(r'__agudoo__', 'ó', palavra)
    palavra = re.sub(r'__agudou__', 'ú', palavra)
    palavra = re.sub(r'__cedilha__', 'ç', palavra)
    return palavra

# BUSCA MUNICIPIOS COM MAIORES DÉFICITS NO ANO
# def municipios_by_saldo_negativo(request):
#     try:
#         municipio = Municipio.objects.filter().values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'funcao_receita_codigo__tipo', 'ano').annotate(valor_total = Sum('valor')).order_by('-valor_total')
#     except Municipio.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = MunicipioSerializer(municipio, many=True)
#         return JsonResponse(serializer.data, safe=False)
