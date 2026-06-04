"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctrl<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

Teoria:
- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)
- A superclasse abstrata precisa ter pelo menos um método abstrato
- As subclasses concretas tem que implementar todos os métodos
  abstratos da superclasse abstrata.
- Precisa importar o módulo abc (abstract base classes)
from abc import ABC, abstractmethod

- Problema (Meet: vbc-shqr-wxd):

- O problema da figura geométrica e o cálculo da área e do perímetro.
O gerente do sistema precisa implantar a RN (regra de negócio) que toda
subclasse incluída no sistema precisa ter a funcionalidade de cálculo
da área e de cálculo do perímetro.

- Com base nos conceitos de Programação Orientada a Objetos (POO),
inheritance (herança) e classe abstrata, implemente um projeto com:
Classe abstrata:
- Forma geométrica
E com as especificidades (classes concretas):
- Quadrado
- Círculo

- Algumas características (atributos) de um Quadrado e Circulo:
cor, lado e raio

- Levante as características (atributos) comuns de um Quadrado e Circulo:
cor

- Levante as características (atributos) específicas de cada figura geométrica:
Quadrado: lado
Círculo: raio

- Vamos trabalhar com dois arquivos.py:
Um arquivo.py com as classes, os construtores e os métodos (defs) e
um segundo arquivo.py com o main e a execução da classe.

- Implemente (Meet: vbc-shqr-wxd):
from abc import ABC, abstractmethod
1a- Crie a superclasse abstrata FormaGeometrica que herda de ABC (Abstract Base Classes)
1b- Crie o método construtor (__init__) com o atributo comum cor.
1c- Crie o método get e método set do atributo cor da superclasse.
2- Crie dois métodos abstratos na superclasse: area e perímetro
2- Crie dois métodos abstratos: area e perímetro
3- Crie um objeto da superclasse abstrata FormaGeometrica, teste
4- Crie a subclasse concreta Quadrado que herda da superclasse abstrata FormaGeometrica
5- crie o construtor com os atributos cor, lado e pelo menos um valor default, teste
6- crie os métodos get e set, teste
7- Sobrescreva o método abstrato area da superclasse abstrata FormaGeometrica
   Fórmula:     area = lado ao quadrado.
8- Crie um objeto da subclasse Quadrado, teste. Porque deu erro?
9- Sobrescreva também o método abstrato perímetro da superclasse abstrata
   Fórmula:     perímetro = 4 . lado
10- Crie um objeto da subclasse Quadrado, teste. Porque não deu erro.
11- Altere o valor do lado, teste
12- crie a subclasse Circulo que herda da superclasse abstrata FormaGeometrica
13- Crie o construtor com os atributos cor e raio e pelo menos um valor default, teste
14- Crie os métodos get e set, teste
15- Sobrescreva o método abstrato area da superclasse abstrata FormaGeometrica
    Fórmula:    área = π . raio ao quadrado
16- Instancie um objeto da subclasse Circulo, teste
17- Sobrescreva também o método perímetro da superclasse abstrata
    Fórmula:    perímetro = 2 . π . raio
18- Instancie um objeto da subclasse Circulo, teste
19- Refaça a subclasse Circulo com a constante pi do Python, mostre com duas casas decimais

- Resposta 19:
import math                     # Como usar:    math.pi
from math import pi             # Como usar:    pi

class Circulo(FormaGeometrica):
    ...
    # Refaça usando a constante PI do Python
    def area(self):
        # vl_area = 3.14 * pow(self.raio, 2)
        # vl_area = pi * pow(self.raio, 2)          # pi, constante do Python
        vl_area = math.pi * pow(self.raio, 2)     # math.pi, constante do Python
        return vl_area

"""

from abc import ABC, abstractmethod # Importa o módulo abc (abstract base classes)
class FormaGeometrica(ABC):         # Classe abstrata, herda da classe ABC
    def __init__(self, cor):        # Atributo de instância
        self.cor = cor
    # Método abstrato, obrigatório pelo menos um na superclasse abstrata
    def get_cor(self):
        return self.cor
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    @abstractmethod                 # Decorator
    def area(self):                 # Método abstrato
        ...                         # Equivalente: pass
    @abstractmethod                 # Decorator
    def perimetro(self):            # Método abstrato
        pass                        # Equivalente: ...

# A subclasse concreta Quadrado herda da superclasse abstrata FormaGeometrica
class Quadrado(FormaGeometrica): # class NomeSubclasse(NomeSuperclasse): # sintaxe
    def __init__(self, cor, lado=2): # Construtor com valor default (padrão)
        super().__init__(cor)        # Chama construtor da superclasse
        self.lado = lado
    def get_lado(self):
        return self.lado
    def set_lado(self, valor):
        self.lado = valor
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def area(self):                  # Obrigatório sobrescrever o método abstrato
        vl_area = self.lado ** 2     # vl_area = self.lado * self.lado
        return vl_area
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def perimetro(self):             # Obrigatório sobrescrever o método abstrato
        vl_perimetro = 4 * self.lado
        return vl_perimetro

# A subclasse concreta Circulo herda da superclasse abstrata FormaGeometrica
class Circulo(FormaGeometrica): # class NomeSubclasse(NomeSuperclasse): # sintaxe
    def __init__(self, cor, raio=1):    # Construtor com valor default (padrão)
        super().__init__(cor)           # Chama construtor da superclasse
        self.raio = raio                # Atributo
    def get_raio(self):
        return self.raio
    def set_raio(self, valor):
        self.raio = valor
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def area(self):                     # Obrigatório sobrescrever o método abstrato
        vl_area = 3.14 * pow(self.raio, 2) # vl_area = 3.14 * self.raio ** 2
        return vl_area
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def perimetro(self):                # Obrigatório sobrescrever o método abstrato
        vl_perimetro = 2 * 3.14 * self.raio
        return vl_perimetro
