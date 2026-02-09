from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Chamado
from .models import Categoria

from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "core/home.html" ) 



def listarChamados(request):
    # Busca TODOS os registros do banco de dados
    chamados = Chamado.objects.all() 
    return render(request, 'core/lista_chamados.html', {"chamados": chamados})



def fechar_chamado(request, id):
    chamado = Chamado.objects.get(id=id)
    chamado.delete()
    print(f"Fechando chamado {chamado.id} - {chamado.problema}")
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/lista_chamados'>Voltar</a>")
    
def novoChamado(request):
    if request.method == "POST":
        laboratorio = request.POST.get('laboratorio')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        categoria = request.POST.get('categoria')

        print("chegou um post")
        print(f"Laboratório: {laboratorio}, Descrição: {problema}")

        Chamado.objects.create(laboratorio=laboratorio, problema=problema, prioridade=prioridade, categoria=categoria)
        
       
        return redirect('/lista_chamados')

    if request.method == "GET":
        print("chegou um get")
        return render(request, 'core/novo_chamado.html', {"categorias": Categoria.objects.all()})



def fechar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    print(f"Fechando categoria {categoria.id} - {categoria.nome}")
    return HttpResponse(f"✅ Categoria removida com sucesso! <br> <a href='/lista-categorias/'>Voltar</a>")

def listarCategorias(request):
    categorias = Categoria.objects.all() 
    return render(request, 'core/lista-categorias.html', {"categorias": categorias})

def novaCategoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Categoria.objects.create(nome=nome, descricao=descricao)
        # salvar meus dados
        return redirect('/lista-categorias')
    return render(request, 'core/nova_categoria.html')

def excluir_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    return redirect('/lista-categorias')

def editar_chamado(request, id):
    chamado =Chamado.objects.get(id=id)
    if request.method == "POST":
        chamado.laboratorio = request.POST.get('laboratorio')
        chamado.problema = request.POST.get('problema')
        chamado.prioridade = request.POST.get('prioridade')
        chamado.categoria = request.POST.get('categoria')
        chamado.save()
        return redirect('/lista_chamados')
    return render(request, 'core/editar_chamado.html', {"chamado": chamado, "categorias": Categoria.objects.all()}) 