from abc import ABC, abstractmethod
#Exercicio 1

class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass


class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        return f"Pagamento de R$ {self.valor} processado com cartão."


class PagamentoBoleto(Pagamento):
    def processar_pagamento(self):
        return f"Pagamento de R$ {self.valor} processado com boleto bancário."
    
def pagamentos():
    cartao = PagamentoCartao(150)
    boleto = PagamentoBoleto(75.50)
    print(cartao.processar_pagamento())
    print(boleto.processar_pagamento())

pagamentos()

#Exercicio 2
class Veiculo(ABC):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)

    def acelerar(self):
        print(f"O carro {self.modelo} do ano {self.ano} está acelerando.")

    def frear(self):
        print(f"O carro {self.modelo} do ano {self.ano} está freando.")

class Moto(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)

    def acelerar(self):
        print(f"A moto {self.modelo} do ano {self.ano} está acelerando.")

    def frear(self):
        print(f"A moto {self.modelo} do ano {self.ano} está freando.")

class Caminhao(Veiculo):
    def __init__(self, modelo, ano):
        super().__init__(modelo, ano)

    def acelerar(self):
        print(f"O caminhão {self.modelo} do ano {self.ano} está acelerando.")

    def frear(self):
        print(f"O caminhão {self.modelo} do ano {self.ano} está freando.")

carro = Carro("Ferrari", 2017)
carro.acelerar()
carro.frear()

#Exercicio 3