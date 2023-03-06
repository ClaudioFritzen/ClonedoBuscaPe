from django.shortcuts import render, HttpResponse


# Create your views here.

def pesquisar(request):
    #return HttpResponse('<h1>Ola mundo!</h1> <br> <hr>')
    return render(request, 'produtos/pesquisa.html')


def exibir_resultados(request):
    pass