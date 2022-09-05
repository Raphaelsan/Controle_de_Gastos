from django.forms import ModelForm
from .models import Transacao, Categoria, Fonte, Credito


class Transacaoform(ModelForm):
    class Meta:
        model = Transacao
        fields = ['descrição', 'data', 'valor', 'categoria', 'observações']


class Categoriaform(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'dt_criacao']


class Creditoform(ModelForm):
     class Meta:
         model = Credito
         fields = ['valor', 'fonte', 'observações', 'data', 'descrição']


class Fonteform(ModelForm):
    class Meta:
        model = Fonte
        fields = ['nome', 'dt_criacao']
