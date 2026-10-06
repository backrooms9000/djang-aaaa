from django.shortcuts import render


def index(request):

    contexto = {
        'nome': 'john',
        'idade':30,
        'frutas': ['maça', 'banana', 'laranja', 'uva', 'caja', 'manga'],
    }

    return render(
        request,
        'cadastro/index.html',
        contexto
    )


def contato(request):

    contexto = {
        "nome": "wyiro",
    }

    return render(
        request,
        'cadastro/contato.html',
        contexto
    )
