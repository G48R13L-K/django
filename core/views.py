import html
from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    return render(request, "core/home.html", {"html": html})

chamados = [
    {"lab": "lab01", "problema": "Computador não liga", "prioridade": "Alta"},
    {"lab": "lab02", "problema": "Internet lenta", "prioridade": "Média"},
    {"lab": "lab03", "problema": "Impressora sem papel", "prioridade": "Baixa"},
]

def listar(request):
    return render(request, "core/listar.html", {"chamados": chamados})



def fechar_chamado( index):
    if 0 <= index < len(chamados):
        del chamados[index]
    return redirect('/listar')
    
def novoChamado(request): 
   
    if request.method == "POST":

        laboratorio = request.POST.get('laboratorio')
        prolema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        
        print(f"Recebido: {laboratorio}, {prolema}, {prioridade}") 

        chamados.append({
            "lab": laboratorio,
            "problema": prolema,
            "prioridade": prioridade
        })

        
        return redirect('/listar')

    return render(request, 'core/novo_chamado.html')
