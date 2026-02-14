from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Chamado
from .models import Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    return render(request, "core/home.html" ) 


@login_required
@permission_required('core.lista_chamados', raise_exception=True)
def listarChamados(request):
    # Busca TODOS os registros do banco de dados
    chamados = Chamado.objects.all() 
    return render(request, 'core/lista_chamados.html', {"chamados": chamados})


@login_required
@permission_required('core.delete_chamado', raise_exception=True)
def fechar_chamado(request, id):
    chamado = Chamado.objects.get(id=id)
    chamado.delete()
    messages.success(request, 'Chamado fechado com sucesso.')
    return redirect('/lista_chamados')
    
def novoChamado(request):
    if request.method == "POST":
        id = request.POST.get('id')
        laboratorio = request.POST.get('laboratorio')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))

        Chamado.objects.create(id=id,laboratorio=laboratorio, problema=problema, prioridade=prioridade, categoria=categoria)
        messages.success(request,' Chamado criado com sucesso.') 
       
        return redirect('/lista_chamados')

    if request.method == "GET":
        print("chegou um get")
        return render(request, 'core/novo_chamado.html', {"categorias": Categoria.objects.all()})


@login_required
def fechar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    print(f"Fechando categoria {categoria.id} - {categoria.nome}")
    messages.success(request, 'Categoria fechada com sucesso.')
    return redirect('/lista-categorias/')

# def listarCategorias(request):
#     categorias = Categoria.objects.all() 
#     return render(request, 'core/lista-categorias.html', {"categorias": categorias})
class ListarCategoriaView(ListView):
    model = Categoria
    template_name  = 'core/lista-categorias.html'
    context_object_name = 'categorias'

def novaCategoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        Categoria.objects.create(nome=nome, descricao=descricao)
        messages.success(request,'Categoria criada com sucesso.')
        # salvar meus dados
        return redirect('/lista-categorias')
    return render(request, 'core/nova_categoria.html')

@login_required
def excluir_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    messages.success(request,'Categoria excluida com sucesso.')
    return redirect('/lista-categorias')

@login_required
def editar_chamado(request, id):
    chamado =Chamado.objects.get(id=id)
    if request.method == "POST":
        chamado.laboratorio = request.POST.get('laboratorio')
        chamado.problema = request.POST.get('problema')
        chamado.prioridade = request.POST.get('prioridade')
        chamado.categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        chamado.save()
        messages.success(request,'Chamado alterado com sucesso.')
        return redirect('/lista_chamados')
    return render(request, 'core/editar_chamado.html', {"chamado": chamado, "categorias": Categoria.objects.all()}) 

@login_required
def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        categoria.nome = request.POST.get('nome')
        categoria.descricao = request.POST.get('descricao')
        categoria.save()
        messages.success(request,'Categoria editada com sucesso.')
        return redirect('/lista-categorias')
    return render(request, 'core/editar_categoria.html', {"categoria": categoria})

def api_chamados(request):
    chamados = Chamado.objects.all()
    data = []
    for chamado in chamados:
        data.append({
            'id': chamado.id,
            'laboratorio': chamado.laboratorio,
            'descricao': chamado.problema,
            'prioridade': chamado.prioridade,
            'categoria': chamado.categoria.nome,
        })
    return JsonResponse(data, safe=False)  