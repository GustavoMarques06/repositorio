#Exercicio 1
class Hospede:
    def __init__(self, nome, cpf, nascimento):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

class ReservaHotel:
    def __init__(self, hospede, numero_quarto, diaria, duracao):
        self.hospede = hospede
        self.numero_quarto = numero_quarto
        self.diaria = diaria
        self.duracao = duracao

    def calcular_custo_total(self):
        return self.diaria * self.duracao

    def exibir_detalhes_reserva(self):
        return f"""
        Hóspede: {self.hospede.nome}
        CPF: {self.hospede.cpf} 
        Data de Nascimento: {self.hospede.nascimento}
        Número do Quarto: {self.numero_quarto}
        Duração da Estadia: {self.duracao} dias
        Custo Total: R$ {self.calcular_custo_total()}

""" 
            
        
        

hospede = Hospede("Jorge", "423.471.851-66", "21/01/1990")
reserva = ReservaHotel(hospede, 101, 150.00, 5)

detalhes_reserva = reserva.exibir_detalhes_reserva()
print(detalhes_reserva)

#Exercicio 2
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = {}  

    def adicionar_item(self, descricao, valor):
        if descricao in self.itens:
            self.itens[descricao] += valor  
        else:
            self.itens[descricao] = valor

    def calcular_valor_total(self):
        return sum(self.itens.values())

    def exibir_detalhes(self):
        detalhes = f"Cliente: {self.cliente.nome} \n Endereço: {self.cliente.endereco} \n Itens do Pedido:\n"
        for descricao, valor in self.itens.items():
            detalhes += f"- {descricao}: R$ {valor}\n"
        detalhes += f"Valor Total: R$ {self.calcular_valor_total()}"
        return detalhes


class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)


class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.restaurantes_favoritos = []

    def adicionar_restaurante_favorito(self, restaurante):
        if self.restaurantes_favoritos.count(restaurante) == 0:
            self.restaurantes_favoritos.append(restaurante)

    def listar_favoritos(self):
        return [restaurante.nome for restaurante in self.restaurantes_favoritos]
    
#Exercicio 3
from datetime import datetime

class Membro:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome},  {self.email}"


class Projeto:
    def __init__(self, nome, data_inicio):
        self.nome = nome
        self.data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
        self.data_termino = 0
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def definir_data_termino(self, data_termino):
        self.data_termino = datetime.strptime(data_termino, "%Y-%m-%d")

    def calcular_duracao(self):
        if self.data_termino:
            duracao = (self.data_termino - self.data_inicio).days
            return duracao
        else:
            return 

    def exibir_detalhes(self):
        detalhes = f"Projeto: {self.nome}\n"
        detalhes += f"Data de Início: {self.data_inicio.strftime('%Y-%m-%d')}\n"
        if self.data_termino:
            detalhes += f"Data de Término: {self.data_termino.strftime('%Y-%m-%d')}\n"
            detalhes += f"Duração: {self.calcular_duracao()} dias\n"
        else:
            detalhes += "Data de Término: Não definida\n"
        
        detalhes += "Membros:\n"
        for membro in self.membros:
            detalhes += f"- {membro}\n"
        
        return detalhes

#exercicio 4
from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.data_criada = datetime.now()  
        self.concluida = False 

    def concluir(self):
        self.concluida = True

    def esta_atrasada(self, prazo_limite):
        prazo_limite_dt = datetime.strptime(prazo_limite, "%Y-%m-%d")
        return not self.concluida and datetime.now() >= prazo_limite_dt

    def exibir_detalhes(self):
        concluida = "Concluída" if self.concluida else "Não Concluída"
        return f"""
            Descrição: {self.descricao}
            Data de Criação: {self.data_criada.strftime("%Y-%m-%d")}
            Status: {concluida}
            """

#exercicio 5

from abc import ABC, abstractmethod

class MetodosPagamento(ABC):
    @abstractmethod
    def processar_valor(self, valor):
        pass


class Pix(MetodosPagamento):
    def processar_valor(self, valor):
        return f"Pix de {valor} R$ foi processado."


class Debito(MetodosPagamento):
    def processar_valor(self, valor):
        return f"Pagamento de R$ {valor} processado via cartão de débito."


class Credito(MetodosPagamento):
    def processar_valor(self, valor):
        return f"Pagamento de R$ {valor} processado via cartão de crédito."

def realizar_pagamento(metodo_pagamento, valor):
    resultado = metodo_pagamento.processar_valor(valor)
    print(resultado)


pix = Pix()
realizar_pagamento(pix, 25)

debito = Debito()
realizar_pagamento(debito, 123.41)

credito = Credito()
realizar_pagamento(credito, 213)


#exercicio 6
