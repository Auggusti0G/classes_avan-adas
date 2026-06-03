"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema:
- Com base nos conceitos de Programação Orientada a Objetos (POO)
e inheritance (herança), implemente a entidade veículo com as
especializações de carro e moto.

- Precisamos trabalhar com estas características (atributos):
valor, quilometragem, quantidade de portas e cilindradas.

- Levante as características (atributos) comuns de um carro e de uma moto:
valor, quilometragem

- Levante as características (atributos) específicas de um carro e de uma moto:
Carro: quantidade de portas;
Moto: cilindradas

- Vamos trabalhar com dois arquivos.py:
Um arquivo.py com as classes, os construtores e os métodos (defs) e
um segundo arquivo.py com o main e a execução da classe.

-Implemente (Meet: vbc-shqr-wxd):
1- Implemente a superclasse Veiculo num arquivo.py separado do main.
2- Crie o método construtor (__init__) com os atributos comuns valor e
   km que indica quilometragem. Ele recebe os parâmetros que serão
   armazenados nos atributos da classe: valor e km.
class NomeClasse:
    def __init__ (self, parametro1, parametro2): # Sintaxe do construtor
        self.atributo1 = parametro1              # Atributos da classe
        self.atributo2 = parametro2
3- No método main, crie (instancie) dois objetos da classe e passe os argumentos
- Obs.: Implemente o main num segundo arquivo.py, separado das classes
# Sintaxe:
from nome_outro_arquivo_sem_extensao import NomeClasse
if __name__ == '__main__':               # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2) # Cria (instancia) um objeto com dois argumentos
4- No método main, mostre os objetos criados, teste (rode) a classe
   print("Objeto criado:", objeto1)      # Teste

5- Crie os métodos (defs) gets dos atributos para consultar os dados.
   def get_atributo1(self):           # Sintaxe do método get (consulta)
       return self.atributo1
6- No main, use (teste) os métodos gets para consultar os objetos criados
   print("Mensagem:", objeto1.get_atributo1()) # nome_objeto.nome_metodo()
7- Crie os métodos (defs) sets dos atributos para alterar os dados.
   def set_atributo1(self, novo_valor):  # sintaxe do método set (altera)
       self.atributo1 = novo_valor
8- No main, use (teste) os métodos sets para os alterar os objetos criados
   objeto1.set_atributo1(envia o novo valor)   # nome_objeto.nome_metodo(novo_valor)
   print("Mensagem:", objeto1.get_atributo1()) # verifica se alterou na memória

9- Crie a subclasse Carro, que herda da superclasse Veiculo. E o construtor
   com os dois atributos comuns e o atributo específico qtd_portas.
   Use pelo menos um atributo com valor default (padrão). No main, teste
class NomeClasse:
    def __init__ (self, parametro1, parametro2, parametro3=0): # Sintaxe do construtor
        self.atributo3 = parametro3                # Atributos da classe
        super().__init__(parametro1, parametro2)
10- No método main, crie (instancie) dois objetos da subclasse com três e dois argumentos
if __name__ == '__main__':               # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2, arg3) # Cria (instancia) um objeto com 3 argumentos
    objeto2 = NomeClasse(arg1, arg2)       # Cria (instancia) um objeto com 2 argumento
11- Crie os métodos (defs) gets dos atributos para consultar, evite código repetido.
12- No main, use (teste) os métodos gets para consultar os objetos criados
13- Crie os métodos (defs) sets dos atributos para alterar, evite código repetido.
14- No main, use (teste) os métodos sets para os alterar os objetos criados

15- Crie a subclasse Moto, que herda a superclasse Veiculo. E o construtor
    com os dois atributos comuns e o atributo específico cilindradas.
    Use pelo menos um atributo com valor default (padrão). No main, teste
16- No método main, crie (instancie) dois objetos da subclasse com três e dois argumentos.
17- Crie os métodos (defs) gets dos atributos para consultar, evite código repetido.
18- No main, use (teste) os métodos gets para consultar os objetos criados
19- Crie os métodos (defs) sets dos atributos para alterar, evite código repetido.
20- No main, use (teste) os métodos sets para os alterar os objetos criados

21- Crie o método (def) atualiza valor, ele recebe o valor em reais e não retorna
     nada. O método acrescenta o valor recebido ao valor de qualquer veículo. Teste.
     Vamos implementar este método em qual classe?
22- No main, teste o método atualiza valor com objetos de Carro e Moto.
23- Refaça o método (def) atualiza com críticas (filtros) dentro do método.

"""

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Veiculo(object):
# class Veiculo():      # Três formas equivalentes de criar classe
class Veiculo:          # Superclasse
    def __init__(self, valor, km):      # Construtor
        self.valor = valor              # Atributos de instância
        self.km = km
    def get_valor(self):                # Consulta
        return self.valor
    def get_km(self):
        return self.km
    def set_valor(self, novo_valor):    # Sem crítica
        self.valor = novo_valor
    def set_km(self, nova_km):
        self.km = nova_km
    # def set_valor(self, valor):       # Com crítica
    #     if valor > 0:
    #         self.valor = valor
    #     else:
    #         print('Valor negativo.')

    def atualiza_valor(self, vlr_aumento):     # Sem crítica (filtros)
        self.valor = self.valor + vlr_aumento  # self.valor += vlr_aumento
    # def atualiza_valor(self, vlr_aumento):       # Com uma crítica (filtro)
    #     if vlr_aumento > 0:
    #         self.valor = self.valor + vlr_aumento # self.valor += vlr_aumento
    #     else:
    #         print('Erro: valor negativo.')

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class NomeSubclasse(NomeSuperclasse):   # Sintaxe de herança
class Carro(Veiculo):  # A subclasse Carro herda da superclasse Veiculo
    def __init__(self, valor, km, qtd_portas=4): # Construtor com valor default
        super().__init__(valor, km)     # Chama construtor da superclasse
        self.qtd_portas = qtd_portas    # Atributo específico da subclasse Carro
    def get_qtd_portas(self):           # Médoto get especpifico da subclasse Carro
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd): # Médoto set especpifico da subclasse Carro
        self.qtd_portas = nova_qtd

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class NomeSubclasse(NomeSuperclasse):  # Sintaxe de herança
class Moto(Veiculo):          # A subclasse Moto herda da superclasse Veiculo
    def __init__(self, valor, km, cilindradas=0):  # Construtor com valor default
        super().__init__(valor, km)     # Chama o construtor da superclasse
        self.cilindradas = cilindradas  # Atributo específico da subclasse Moto
    def get_cilindradas(self):          # Médoto get especpifico da subclasse Moto
        return self.cilindradas
    def set_cilindradas(self, novo_valor): # Médoto set especpifico da subclasse Moto
        self.cilindradas = novo_valor
