# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClassificacaoDespesa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'classificacao_despesa'


class ClassificacaoReceita(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'classificacao_receita'


class Despesa(models.Model):
    codigo = models.AutoField(primary_key=True)
    ano = models.IntegerField()
    valor = models.FloatField()
    classificacao_despesa_codigo = models.ForeignKey(ClassificacaoDespesa, models.DO_NOTHING, db_column='classificacao_despesa_codigo')
    municipio_codigo = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_codigo')
    funcao_despesa_codigo = models.ForeignKey('FuncaoDespesa', models.DO_NOTHING, db_column='funcao_despesa_codigo')

    class Meta:
        managed = False
        db_table = 'despesa'


class FuncaoDespesa(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'funcao_despesa'


class FuncaoReceita(models.Model):
    codigo = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=170)

    class Meta:
        managed = False
        db_table = 'funcao_receita'


class Municipio(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=70)
    uf = models.CharField(max_length=2)
    regiao = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'municipio'


class Receita(models.Model):
    codigo = models.AutoField(primary_key=True)
    ano = models.IntegerField()
    valor = models.FloatField()
    municipio_codigo = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='municipio_codigo')
    funcao_receita_codigo = models.ForeignKey(FuncaoReceita, models.DO_NOTHING, db_column='funcao_receita_codigo')
    classificacao_receita_codigo = models.ForeignKey(ClassificacaoReceita, models.DO_NOTHING, db_column='classificacao_receita_codigo')

    class Meta:
        managed = False
        db_table = 'receita'
