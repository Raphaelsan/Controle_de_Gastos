from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(max_length=50)
    def __str__(self):
        return self.nome

class Fonte(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(max_length=50)
    def __str__(self):
        return self.nome


class Credito(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE)
    descrição = models.CharField(max_length=200)
    observações = models.TextField(null=True, blank=True)
    data = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Créditos'

    def __str__(self):
        return self.descrição


class Transacao(models.Model):
    data = models.DateTimeField()
    descrição = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observações = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Transações'


    def __str__(self):
        return self.descrição

# Create your models here.
