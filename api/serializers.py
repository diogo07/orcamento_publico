from rest_framework import serializers
from api.models import Municipio

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class ReceitaSerializer(serializers.ModelSerializer):
    codigo = serializers.IntegerField(read_only=True)
    ano = serializers.IntegerField(read_only=True)
    valor = serializers.FloatField(read_only=True)
    municipio_codigo = serializers.IntegerField(read_only=True)
    funcao_receita_codigo = serializers.IntegerField(read_only=True)
    classificacao_receita_codigo = serializers.IntegerField(read_only=True)
    valor_total = serializers.FloatField(read_only=True)