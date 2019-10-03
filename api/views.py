from api.models import Municipio, Receita, Despesa
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from api.serializers import MunicipioSerializer
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
        despesas = Despesa.objects.filter(municipio_codigo=codigo_municipio).values('municipio_codigo__nome', 'municipio_codigo__uf', 'municipio_codigo__regiao', 'ano', 'classificacao_despesa_codigo__tipo').annotate(valor_total = Sum('valor')).order_by('ano')

        context = []
        dados = []

        for despesa in despesas:
            dados.append(
                {
                    'ano': despesa['ano'],
                    'classificacao': despesa['classificacao_despesa_codigo__tipo'],
                    'valor': despesa['valor_total']
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
        receitas = Receita.objects.filter(municipio_codigo=codigo_municipio).values('municipio_codigo__nome',
                                                                                    'municipio_codigo__uf',
                                                                                    'municipio_codigo__regiao', 'ano').annotate(
            valor_total=Sum('valor')).order_by('ano')

        context = []
        dados = []

        for receita in receitas:
            dados.append(
                {
                    'ano': receita['ano'],
                    'valor': receita['valor_total']
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

    except Despesa.DoesNotExist:
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

from django.db import connection

def ranking_municipios_por_investimento(request, area, ano):
        with connection.cursor() as cursor:
            cursor.execute("select d.ano, m.nome, m.uf, (case when ((sum(case when fd.codigo = "+str(area)+" then d.valor end)) / sum(d.valor) * 100) is not null then (((sum(case when fd.codigo = "+str(area)+" then d.valor end)) / sum(d.valor) * 100)) else 0.00 end) as porcentagem from despesa as d inner join municipio as m on m.codigo = d.municipio_codigo inner join classificacao_despesa as cd on cd.codigo = d.classificacao_despesa_codigo inner join funcao_despesa as fd on fd.codigo = d.funcao_despesa_codigo where cd.codigo = 2 and ano = "+str(ano)+" group by d.ano, m.nome, m.uf order by porcentagem desc limit 10")
            municipios = cursor.fetchall()

        context = []

        for m in municipios:
            context.append({
                'ano': m[0],
                'municipio': m[1],
                'uf': m[2],
                'porcentagem': m[3]
            })

        if request.method == 'GET':
            return JsonResponse(context, safe=False)


def ranking_municipios_por_uf_e_investimento(request, uf, area, ano):
    with connection.cursor() as cursor:
        cursor.execute("select d.ano, m.nome, m.uf, (case when ((sum(case when fd.codigo = " + str(
            area) + " then d.valor end)) / sum(d.valor) * 100) is not null then (((sum(case when fd.codigo = " + str(
            area) + " then d.valor end)) / sum(d.valor) * 100)) else 0.00 end) as porcentagem from despesa as d inner join municipio as m on m.codigo = d.municipio_codigo inner join classificacao_despesa as cd on cd.codigo = d.classificacao_despesa_codigo inner join funcao_despesa as fd on fd.codigo = d.funcao_despesa_codigo where cd.codigo = 2 and m.uf = '" +str(uf)+ "' and ano = " + str(
            ano) + " group by d.ano, m.nome, m.uf order by porcentagem desc limit 10")
        municipios = cursor.fetchall()

    context = []

    for m in municipios:
        context.append({
            'ano': m[0],
            'municipio': m[1],
            'uf': m[2],
            'porcentagem': m[3]
        })

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
#def municipios_by_saldo_negativo(request):