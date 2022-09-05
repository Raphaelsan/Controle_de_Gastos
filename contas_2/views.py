from django.shortcuts import render, redirect
import datetime
from .models import Transacao, Credito
from .form import Transacaoform, Categoriaform, Fonteform, Creditoform


def home(request):
    data = {}
    lista = []

    for c in range(10):
        lista.append(c+1)

    data['transacoes'] = [lista]
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)


def nova_transacao(request):
    data = {}
    form = Transacaoform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)


def nova_transacao_e(request):
    data = {}
    form = Creditoform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)


def nova_categoriaf(request):
    data = {}
    form = Fonteform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)



def nova_categoria(request):
    data = {}
    form = Categoriaform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form

    return render(request, 'contas/form.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    data['transacoes_e'] = Credito.objects.all()

    return render(request, 'contas/listagem.html', data)


def saldo(request):
    data = {}
    data['entradas'] = Transacao.objects.all()
    data['saídas'] = Credito.objects.all()
    entrada = data['entradas']
    saida = data['saídas']

    return render(request, 'contas/listagem.html', data)


def updatet(request, pk):
    data = {}

    transacao = Transacao.objects.get(pk=pk)
    form = Transacaoform(request.POST or None, instance=transacao)  # Dessa maneira o formulário nunca estará vazio,
    # ou receberá oque o usuário inputar ou através do objeto pego no banco
    if form.is_valid():
         form.save()
         return redirect('url_listagem')


    data['form'] = form
    data['transação'] = transacao

    return render(request, 'contas/form.html', data)


def update(request, pk):
    data = {}

    transacao2 = Credito.objects.get(pk=pk)
    form2 = Creditoform(request.POST or None, instance=transacao2)  # Dessa maneira o formulário nunca estará vazio,
    # ou receberá oque o usuário inputar ou através do objeto pego no banco

    if form2.is_valid():
        form2.save()
        return redirect('url_listagem')

    data['form'] = form2
    data['transação'] = transacao2

    return render(request, 'contas/form.html', data)


def delete(request, pk):
    transacao = Transacao.objects.filter(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
