import html
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from core.models import Chamado



def home(request):
    return render(request, "core/home.html", {"html": html})

chamados = [
    {"id": 1, "lab": "lab01", "categoria": "Hardware", "problema": "Computador não liga", "prioridade": "Alta"},
    {"id": 2, "lab": "lab02", "categoria": "Software", "problema": "Internet lenta", "prioridade": "Média"},
    {"id": 3, "lab": "lab03", "categoria": "Hardware", "problema": "Impressora sem papel", "prioridade": "Baixa"},
]

def listarChamados(request):
    return render(request, "core/lista_chamados.html", {"chamados": chamados})



def fechar_chamado(request, id):
    chamado = chamados[id - 1]  # Assuming chamados is a list of dictionaries
    chamados.remove(chamado)
    print(f"Fechando chamado {chamado['id']} - {chamado['problema']}")
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/lista-chamados/'>Voltar</a>")
    
def novoChamado(request): 
   
    if request.method == "POST":

        laboratorio = request.POST.get('laboratorio')
        prolema = request.POST.get('problema')
        categoria = request.POST.get('categoria')
        prioridade = request.POST.get('prioridade')
        
        print(f"Recebido: {laboratorio}, {prolema}, {prioridade}") 

        chamados.append({
            "id": len(chamados) + 1,
            "lab": laboratorio,
            "categoria": categoria,
            "problema": prolema,
            "prioridade": prioridade
        })

        
        return redirect('/lista_chamados/')

    return render(request, 'core/novo_chamado.html', {"categorias_list": categorias_list})

def listarCategorias(request):
    return render(request, "core/lista-categorias.html", {"categorias": categorias_list})

categorias_list = [
    {"id": 1, "nome": "Hardware", "descricao": "Problemas relacionados a componentes físicos"},
    {"id": 2, "nome": "Software", "descricao": "Problemas relacionados a programas e aplicativos"}
]
def novaCategoria(request):
    if request.method == "POST":
        id = len(categorias_list) + 1
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categorias_list.append({
            "id": id,
            "nome": nome,
            "descricao": descricao
        })
        print(f"Nova categoria criada: {nome}, {descricao}")
        return HttpResponse(f"✅ Categoria '{nome}' criada com sucesso! <br> <a href='/lista-categorias/'>Voltar</a>")   
    
    return render(request, 'core/nova_categoria.html')

def fechar_categoria(request, id):
    categoria = categorias_list[id - 1]  # Assuming categorias_list is a list of dictionaries
    categorias_list.remove(categoria)
    print(f"Fechando categoria {categoria['id']} - {categoria['nome']}")
    return HttpResponse(f"✅ Categoria removida com sucesso! <br> <a href='/lista-categorias/'>Voltar</a>")