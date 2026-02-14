from django.db import models
 

             
class Categoria(models.Model):
        # Texto curto (max 100 letras)
        nome = models.CharField(max_length=100)
        descricao = models.TextField(blank=True, null=True)
            
        # Data e Hora automática no momento da criação
        data_criacao = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.nome} - {self.descricao} - {self.data_criacao} "
    
class Equipamento(models.Model):
        
        descricao = models.CharField(max_length=100)
        tipo = models.CharField(max_length=50)
        ocupado = models.BooleanField()

        opcoes_condicao = [
            ('Novo', 'Novo'),
            ('Usado', 'Usado'),
            ('Defeituoso', 'Defeituoso'),
        ]
        condicao = models.CharField(max_length=20, choices=opcoes_condicao, default='Novo')    
        data_criacao = models.DateTimeField(auto_now_add=True)        

        def __str__(self):
            return f"{self.descricao} - {self.tipo} - {'Ocupado' if self.ocupado else 'Disponível'} - {self.condicao} - {self.data_criacao}"

class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        cpf = models.IntegerField()
        idade = models.IntegerField()
        dataNascimento = models.DateField()
        cidade = models.CharField(max_length=100)
        estado = models.CharField(max_length=50)
        pais = models.CharField(max_length=50)
        
        opcpoes_genero = [
            ('Masculino', 'Masculino'),
            ('Feminino', 'Feminino'),
            ('Outro', 'Outro'),
        ]
        genero = models.CharField(max_length=20, choices=opcpoes_genero, default='Outro')
        opcpoes_estado_civil = [
            ('Solteiro', 'Solteiro'),
            ('Casado', 'Casado'),
            ('Divorciado', 'Divorciado'),
            ('Viúvo', 'Viúvo'),
        ]
        estado_civil = models.CharField(max_length=20, choices=opcpoes_estado_civil, default='Solteiro')
        altura = models.FloatField()
        peso = models.FloatField()
        emprego = models.CharField(max_length=50)
        data_criacao = models.DateTimeField(auto_now_add=True)      

        def __str__(self):
            return f"{self.nome} - {self.email} - {self.cpf} - {self.data_criacao} - {self.idade} - {self.cidade} - {self.estado} - {self.pais} - {self.genero} - {self.estado_civil} - {self.altura} - {self.peso} - {self.emprego}"

class Chamado(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, null=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.SET_NULL, null=True) 


    # Texto curto (max 100 letras)
    laboratorio = models.CharField(max_length=100)
    
    # Texto longo (sem limite de letras)
    problema = models.TextField()
    
    # Escolhas pré-definidas
    OPCOES_PRIORIDADE = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE, default='media')
    
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.laboratorio} - {self.prioridade} - {self.categoria} - {self.data_criacao} "