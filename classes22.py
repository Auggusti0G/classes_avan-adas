"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema (Meet: vbc-shqr-wxd):

- Com base nos conceitos de Programação Orientada a Objetos (POO) e
inheritance (herança), implemente a entidade conta corrente com as
especificidades de:
conta corrente pessoa física e
conta corrente pessoa jurídica.

- Algumas características (atributos) de uma conta corrente:
nome, saldo, gênero e modalidade de PJ

- Levante as características (atributos) comuns de uma conta corrente:
nome
saldo

- Levante as características (atributos) específicas de cada conta corrente:
ContaCorrentePessoaFisica: gênero
ContaCorrentePessoaJuridica: modalidade de PJ

-Implemente (Meet: vbc-shqr-wxd):
1- Implemente a superclasse Conta num arquivo.py separado do main.
2- Crie o método construtor (__init__) com os atributos comuns nome e
   saldo. O método recebe os parâmetros que serão armazenados nos
   atributos da classe: nome e saldo.
3- Crie os métodos (defs) gets dos atributos para consultar os dados.
   def get_atributo1(self):           # Sintaxe do método get (consulta)
       return self.atributo1
4- Crie os métodos (defs) sets dos atributos para alterar os dados.
   def set_atributo1(self, novo_valor):  # sintaxe do método set (altera)
       self.atributo1 = novo_valor
5- No método main, crie (instancie) objetos da classe e passe os argumentos
- Obs.: implemente o main num segundo arquivo.py, separado das classes
# Sintaxe:
from nome_outro_arquivo_sem_extensao import NomeClasse
if __name__ == '__main__':               # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2) # Cria (instancia) um objeto com argumentos
    print("Endereço do objeto criado:", objeto1)      # Teste
6- No main, use (teste) os métodos gets para consultar os objetos criados
   print("Mensagem:", objeto1.get_atributo1()) # nome_objeto.nome_metodo()
7- No main, use (teste) os métodos sets para os alterar os objetos criados
   objeto1.set_atributo1(envia novo valor)     # nome_objeto.nome_metodo(novo_valor)
   print("Mensagem:", objeto1.get_atributo1()) # verifica se alterou na memória

8- Crie a subclasse conta pessoa física, que herda da superclasse Conta. E o
   construtor com os dois atributos comuns e o atributo específico gênero.
   Use pelo menos um atributo com valor default (padrão).
class NomeSubClasse(NomeSuperClasse):
    def __init__ (self, parametro1, parametro2, parametro3='m'): # Sintaxe do construtor
        self.atributo3 = parametro3                # Atributos da classe
        super().__init__(parametro1, parametro2)
9- No método main, crie (instancie) dois objetos da subclasse com três e dois argumentos
if __name__ == '__main__':                 # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2, arg3) # Cria (instancia) um objeto com 3 argumentos
    objeto2 = NomeClasse(arg1, arg2)       # Cria (instancia) um objeto com 2 argumento
10- Crie os métodos (defs) gets dos atributos para consultar, evite código repetido.
11- No main, use (teste) os métodos gets para consultar os objetos criados
12- Crie os métodos (defs) sets dos atributos para alterar, evite código repetido.
13- No main, use (teste) os métodos sets para os alterar os objetos criados

14- Crie a subclasse conta pessoa jurídica, que herda da superclasse Conta. E o
   construtor com os dois atributos comuns e o atributo específico modalidade.
   Use pelo menos um atributo com valor default (padrão).
15- No método main, crie (instancie) dois objetos da subclasse com três e dois argumentos
16- Crie os métodos (defs) gets dos atributos para consultar, evite código repetido.
17- No main, use (teste) os métodos gets para consultar os objetos criados
18- Crie os métodos (defs) sets dos atributos para alterar, evite código repetido.
19- No main, use (teste) os métodos sets para os alterar os objetos criados

20- Crie o método deposito, ele recebe o valor do depósito e atualiza o saldo.
    Implementar esse método em qual classe? Teste
21- Crie o método retirada, ele recebe o valor da retirada e atualiza o saldo, teste
22- Refaça o método retirada usando RNs (Regras de Negócio) bancárias. Teste

"""

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Conta(object): # Três formas equivalentes de criar classe
# class Conta():
class Conta:                          # Superclasse
    def __init__(self, nome, saldo):  # Construtor
        self.nome = nome              # Atributos de instância (objeto)
        self.saldo = saldo
    def get_nome(self):               # Consulta
        return self.nome
    def get_saldo(self):
        return self.saldo
    def set_nome(self, novo_nome):    # Altera
        self.nome = novo_nome
    # Não implemente o método set_saldo, RN (Regra de Negócio) dos bancos.
    def deposito(self, valor):          # Métodos funcionais
        self.saldo += valor             # self.saldo = self.saldo + valor
    def retirada(self, valor):          # Sem RN (Regra de Negócio)
        self.saldo -= valor             # self.saldo = self.saldo - valor
    def retirada_rn(self, valor):       # RN obrigatória (natural dos bancos)
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse): # Sintaxe
class PessoaFisica(Conta): # Subclasse PessoaFisica herda da superclasse Conta
    def __init__(self, nome, saldo, genero='m'): # Valores default (padrão)
        super().__init__(nome, saldo)   # Chama o construtor da superclasse
        self.genero = genero
    def get_genero(self):               # Consulta
        return self.genero
    def set_genero(self, novo_genero):  # Altera
        self.genero = novo_genero

""" 
- As principais modalidades de PJ:
1 - MEI (Microempreendedor Individual)
2 - ME – Microempresa
3 - EPP (Empresa de Pequeno Porte)
4 - EI (Empresário Individual) 
5 - EIRELI (Empresa Individual de Responsabilidade Limitada)
6 - Sociedade Limitada – LTDA
7 - Sociedade Anônima (SA)                                  """
# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class NomeSubclasse(NomeSuperclasse):   # Sintaxe
class PessoaJuridica(Conta): # Subclasse PessoaJuridica herda da superclasse Conta
    def __init__(self, nome, saldo, modalidade='MEI'): # Construtor com default (padrão)
        super().__init__(nome, saldo) # Chama o construtor da superclasse
        self.modalidade = modalidade
    def get_modalidade(self):                  # Consulta
        return self.modalidade
    def set_modalidade(self, nova_modalidade): # Altera
        self.modalidade = nova_modalidade
