#Exercicio 1
class PessoaJuridica:
    def __init__(self, nome, renda_bruta):
        self.nome = nome
        self.renda_bruta = renda_bruta

    def calcular_imposto(self):
        imposto = self.renda_bruta * 0.10
        return imposto
class PessoaFisica:
    def __init__(self, nome, renda_bruta):
        self.nome = nome
        self.renda_bruta = renda_bruta
    def calcular_imposto(self):
        if self.renda_bruta <= 1400:
            imposto = 0
        elif self.renda_bruta <= 2100:
            imposto = self.renda_bruta * 0.10 - 100
        elif self.renda_bruta <= 2800:
            imposto = self.renda_bruta * 0.15 - 270
        elif self.renda_bruta <= 3600:
            imposto = self.renda_bruta * 0.25 - 500
        else:
            imposto = self.renda_bruta * 0.30 - 700
        return imposto


pessoa1 = PessoaFisica("João Paulo", 120)    
pessoa2 = PessoaFisica("Mario", 2515) 
pessoa3 = PessoaFisica("Carlao", 5151)  

pessoa_juridica1 = PessoaJuridica("X", 50130)   
pessoa_juridica2 = PessoaJuridica("Tesla", 214125) 
pessoa_juridica3 = PessoaJuridica("McDonalds", 25151)

contribuintes = [pessoa1, pessoa2, pessoa3, pessoa_juridica1, pessoa_juridica2, pessoa_juridica3]

for contribuinte in contribuintes:
    print(f"{contribuinte.nome} Renda Bruta: R$ {contribuinte.renda_bruta} Imposto: R$ {contribuinte.calcular_imposto()}")



#Exercicio 2
class Remedio:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def calcular_preco(self):
        return self.valor * 0.80

class RemedioDeMarca(Remedio):
    def __init__(self, nome, valor, marca):
        super().__init__(nome, valor)
        self.marca = marca
    
    def calcular_preco(self):
        return self.valor

class Farmacia:
    def __init__(self):
        self.genericos = []
        self.remedios_de_marca = []
    
    def adicionar_remedio_generico(self, remedio):
        self.genericos.append(remedio)
    
    def adicionar_remedio_de_marca(self, remedio):
        self.remedios_de_marca.append(remedio)
    
    def calcular_total_genericos(self):
        return sum([remedio.calcular_preco() for remedio in self.genericos])
    def calcular_total_marca(self):
        return sum([remedio.calcular_preco() for remedio in self.remedios_de_marca])
    def calcular_total_geral(self):
        total_genericos = self.calcular_total_genericos()
        total_marca = self.calcular_total_marca()
        return total_genericos + total_marca


remedio_generico1 = Remedio("Rivotril", 125.00)  
remedio_generico2 = Remedio("Dorflex", 10.00)   
remedio_generico3 = Remedio("Dipirona", 112.00)     

remedio_marca1 = RemedioDeMarca("Aspirina", 45.00, "RemediosTop") 
remedio_marca2 = RemedioDeMarca("Cefagel", 50.00, "Johnson") 

farmacia = Farmacia()
farmacia.adicionar_remedio_generico(remedio_generico1)
farmacia.adicionar_remedio_generico(remedio_generico2)
farmacia.adicionar_remedio_generico(remedio_generico3)
farmacia.adicionar_remedio_de_marca(remedio_marca1)
farmacia.adicionar_remedio_de_marca(remedio_marca2)


print(f"Total de remédios genéricos: R$ {farmacia.calcular_total_genericos():.2f}")
print(f"Total de remédios de marca: R$ {farmacia.calcular_total_marca():.2f}")
print(f"Total geral: R$ {farmacia.calcular_total_geral():.2f}")

#Exercicio 3

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def calcular_preco(self):
        return self.preco

class Livro(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
    
    def calcular_preco(self):
        return self.preco * 0.90

class Eletronico(Produto):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
    
    def calcular_preco(self):
        return self.preco * 1.15

class Roupa(Produto):
    def __init__(self, nome, preco, importada, da_estacao):
        super().__init__(nome, preco)
        self.importada = importada
        self.da_estacao = da_estacao
    
    def calcular_preco(self):
        preco_final = self.preco
        if self.importada:
            preco_final *= 1.05 
        if self.da_estacao:
            preco_final *= 0.80 
        return preco_final

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        total = sum([produto.calcular_preco() for produto in self.produtos])
        return total


livro = Livro("Diario de um Banana", 50.00)  
eletronico = Eletronico("Iphone 20", 9700.00)  
roupa_importada = Roupa("Camisa Do Corinthians", 420.00, True, True) 
roupa_nao_importada = Roupa("Calca Nike", 480.00, False, False)  

carrinho = Carrinho()
carrinho.adicionar_produto(livro)
carrinho.adicionar_produto(eletronico)
carrinho.adicionar_produto(roupa_importada)
carrinho.adicionar_produto(roupa_nao_importada)

total = carrinho.calcular_total()
print(f"Total do carrinho: R$ {total}")


#Exercicio 4
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.pontuacao_base = 0 

    def calcular_pontuacao(self):
        return self.pontuacao_base

    def calcular_bono(self):
        return self.salario * 0.05  


class FuncionarioVendas(Funcionario):
    def __init__(self, nome, salario, volume_vendas, meta_vendas):
        super().__init__(nome, salario)
        self.volume_vendas = volume_vendas
        self.meta_vendas = meta_vendas
        self.pontuacao_base = self.calcular_pontuacao_vendas()

    def calcular_pontuacao_vendas(self):
        if self.volume_vendas >= self.meta_vendas:
            return 100
        else:
            return int((self.volume_vendas / self.meta_vendas) * 100)

    def calcular_bono(self):
        bonus = super().calcular_bono()
        if self.pontuacao_base > 50:
            bonus += self.salario * 0.10  
        return bonus


class FuncionarioTecnologia(Funcionario):
    def __init__(self, nome, salario, projetos_completos, prazos_cumpridos):
        super().__init__(nome, salario)
        self.projetos_completos = projetos_completos
        self.prazos_cumpridos = prazos_cumpridos
        self.pontuacao_base = self.calcular_pontuacao_tecnologia()

    def calcular_pontuacao_tecnologia(self):
        return min(self.projetos_completos * 10, 100)  

    def calcular_bono(self):

        bonus = super().calcular_bono()
        if self.prazos_cumpridos:
            bonus += self.salario * 0.09  
        return bonus


class FuncionarioAdministrativo(Funcionario):
    def __init__(self, nome, salario, avaliacoes_anuais, metas_atingidas):
        super().__init__(nome, salario)
        self.avaliacoes_anuais = avaliacoes_anuais
        self.metas_atingidas = metas_atingidas
        self.pontuacao_base = self.calcular_pontuacao_administrativo()

    def calcular_pontuacao_administrativo(self):
        return min(self.avaliacoes_anuais * 10, 100)

    def calcular_bono(self):

        bonus = super().calcular_bono()
        if self.metas_atingidas:
            bonus += self.salario * 0.08 
        return bonus


class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def avaliar_funcionarios(self):
        resultados = []
        for funcionario in self.funcionarios:
            pontuacao = funcionario.calcular_pontuacao()
            bonus = funcionario.calcular_bono()
            resultados.append({
                "Nome": funcionario.nome,
                "Pontuação de Desempenho": pontuacao,
                "Bônus": round(bonus, 2)
            })
        return resultados


funcionario1 = FuncionarioVendas("Jao", 4500, 910, 100)  
funcionario2 = FuncionarioVendas("Caio", 76000, 320, 100)  
funcionario3 = FuncionarioTecnologia("Gustavo", 13000, 4, True)  
funcionario4 = FuncionarioAdministrativo("Julio", 31500, 2, True)  

empresa = Empresa()
empresa.adicionar_funcionario(funcionario1)
empresa.adicionar_funcionario(funcionario2)
empresa.adicionar_funcionario(funcionario3)
empresa.adicionar_funcionario(funcionario4)

resultados = empresa.avaliar_funcionarios()

for resultado in resultados:
    print(f"Nome: {resultado['Nome']}")
    print(f"Pontuação de Desempenho: {resultado['Pontuação de Desempenho']}")
    print(f"Bônus: R$ {resultado['Bônus']}\n")

#Exercicio 5
class Recurso:
    def __init__(self, nome):
        self.nome = nome

    def calcular_custo(self, dias):
        return 0


class RecursoHumano(Recurso):
    def __init__(self, nome, taxa_diaria):
        super().__init__(nome)
        self.taxa_diaria = taxa_diaria

    def calcular_custo(self, dias):
        return self.taxa_diaria * dias


class RecursoEquipamento(Recurso):
    def __init__(self, nome, taxa_diaria, custo_instalacao):
        super().__init__(nome)
        self.taxa_diaria = taxa_diaria
        self.custo_instalacao = custo_instalacao

    def calcular_custo(self, dias):
        return self.taxa_diaria * dias + self.custo_instalacao


class RecursoLicencaSoftware(Recurso):
    def __init__(self, nome, taxa_mensal):
        super().__init__(nome)
        self.taxa_mensal = taxa_mensal

    def calcular_custo(self, dias):
        meses = dias / 30  
        return self.taxa_mensal * meses


class Projeto:
    def __init__(self, nome, recursos=None):
        self.nome = nome
        self.recursos = recursos if recursos else []

    def adicionar_recurso(self, recurso):
        self.recursos.append(recurso)

    def calcular_custo_total(self, dias):
        custo_total = 0
        for recurso in self.recursos:
            custo_total += recurso.calcular_custo(dias)
        return custo_total

recurso_humano = RecursoHumano("Jair", 250)  
recurso_equipamento = RecursoEquipamento("PC", 100, 500)  
recurso_licenca = RecursoLicencaSoftware("Windows", 300)  

projeto = Projeto("Projeto 1")
projeto.adicionar_recurso(recurso_humano)
projeto.adicionar_recurso(recurso_equipamento)
projeto.adicionar_recurso(recurso_licenca)

dias = 30
custo_total = projeto.calcular_custo_total(dias)

print(f"Custo total do projeto {projeto.nome} para {dias} dias: R$ {custo_total:.2f}")