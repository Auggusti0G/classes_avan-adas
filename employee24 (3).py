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

- Analise o problema do empregado e o cálculo do salário.

- A superclasse Employee representa um funcionário geral (Fulltime ou
Hourly). Ela deve ser uma classe abstrata e deve ter o método abstrato
calcula salário com a finalidade de obrigar todas as subclasses concretas
do sistema sobrescreverem o método calcula salário com as regras de
negócios (RN) específicas de cada tipo de funcionário.

- Com base nos conceitos de Programação Orientada a Objetos (POO),
inheritance (herança) e classe abstrata, implemente um projeto com:
Classe abstrata:
- Employee
E com as especificidades (classes concretas):
- FulltimeEmployee
- HourlyEmployee

- Algumas características (atributos) de um FulltimeEmployee e HourlyEmployee:
first_name
Last_name
base salary
worked_hours
value_hour

- As características (atributos) comuns de um FulltimeEmployee e HourlyEmployee:
first_name
Last_name

- Levante as características (atributos) específicas de cada figura geométrica:
FulltimeEmployee: base salary
HourlyEmployee: worked_hours, value_hour

- Vamos trabalhar com dois arquivos.py:
Um arquivo.py com as classes, os construtores e os métodos (defs) e
um segundo arquivo.py com o main e a execução da classe.

- Implemente (Meet: vbc-shqr-wxd):
from abc import ABC, abstractmethod
1- Crie a superclasse abstrata Employee que herda de ABC (Abstract Base Classes)
2- Crie o construtor com os atributos first_name e Last_name
3- Crie os métodos gets e sets da superclasse
4- Crie o método abstrato compute_salary
5- Crie o método concreto full_name, ele retorna o nome completo
6- Crie um objeto da superclasse Employee, conseguiu?

7- Crie a subclasse concreta FulltimeEmployee que herda da superclasse abstrata Employee
8- Crie o construtor com os atributos first name, last name e base salary com
   pelo menos um valor default (padrão)
9- crie os métodos get e set, teste
10- Crie um objeto da subclasse FulltimeEmployee passando três argumentos, conseguiu?
11- A Regra de Negócio (RN) do compute_salary do FulltimeEmployee é o base salary
    mais um bônus de 200 reais. Sobrescreva o método abstrato compute_salary
12- Crie um objeto da subclasse FulltimeEmployee, conseguiu?
13- Consulte o primeiro nome, nome completo, salário base e o salário total
14- Crie um objeto da subclasse FulltimeEmployee passando apenas dois argrumentos.

15- Crie a subclasse concreta HourlyEmployee que herda da superclasse abstrata Employee
16- Crie o construtor com os atributos first name, last name, worked_hours e value_hour
    com pelo menos um valor default (padrão)
17- crie os métodos get e set, teste
18- Crie um objeto da subclasse HourlyEmployee passando quatro argumentos, conseguiu?
19- A Regra de Negócio (RN) do compute_salary do HourlyEmployee é
    worked_hours vezes value_hour. Sobrescreva o método abstrato compute_salary
20- Consulte o primeiro nome, nome completo e o salário total
21- Crie um objeto da subclasse HourlyEmployee passando apenas três argumentos, conseguiu?

22- O sistema precisa informar quantos empregados (objetos) foram instanciados
    (cadastrados na memória). Então, crie o atributo de classe.
23- Atualize o construtor para implementar esse requisito (funcionalidade)
24- Crie o método de classe para consultar e retornar a quantidade de empregados
    instanciados (cadastrados). Teste
----------------------------------------------------------
- Resposta do 22, 23 e 24:
    count = 0                           # Atributo de classe
    @classmethod
    def count_employees(cls):           # Método de classe
        return cls.count
    def __init__(self, first_name, last_name): # Construtor
        self.first_name = first_name    # Atributos de instância
        self.last_name = last_name
        Employee.count += 1             # Atualiza o atributo de classe (count)
No main, chame o método de classe assim:
- Sintaxe:
    print("Quantidade de objstos:", NomeClasse.nome_metodo())
- Exemplo:
    print("Quantidade de objstos:", Employee.count_employees())

"""

# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: a primeira letra de cada palavra com letra maiúscula
from abc import ABC, abstractmethod # Importa o módulo abc (abstract base classes)
class Employee(ABC):                # Classe abstrata, herda da classe ABC do Python
    def __init__(self, first_name, last_name): # Construtor
        self.first_name = first_name           # Atributos de instância
        self.last_name = last_name
    def get_first_name(self):                   # Consulta
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def set_first_name(self, new_name):         # Altera
        self.first_name = new_name
    def set_last_name(self, new_name):
        self.last_name = new_name
    # Método abstrato, obrigatório pelo menos um na superclasse abstrata
    @abstractmethod                         # Decorator
    def compute_salary(self):
        pass                                # ...
    def full_name(self):
        full_name = self.first_name + " " + self.last_name  # Concatenação
        fullname = f"{self.first_name} {self.last_name}"    # f-string
        return fullname
        # return f"{self.first_name} {self.last_name}"  # Equivalente

class FulltimeEmployee(Employee):               # class Subclasse(Superclasse):
    def __init__(self, first_name, last_name, base_salary=1500.00): # Valor padrão
        super().__init__(first_name, last_name) # Chama construtor superclasse
        self.base_salary = base_salary          # Atributo de instância
    def get_base_salary(self):                  # Consulta
        return self.base_salary                 # Valor do saláio base
    def set_base_salary(self, new_base_salary): # Altera
        self.base_salary = new_base_salary
    # Método obrigatório, sobrescreve o método abstrato da superclasse
    def compute_salary(self):                   # Cálculo do salário total
        salario_total = self.base_salary + 200  # Bônus de 200 reais
        return salario_total
        # return self.base_salary + 200  # Equivalente as 2 linhas anteriores

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hours_worked, hour_value=300.00): # Valor padrão
        super().__init__(first_name, last_name)   # Chama construtor superclasse
        self.hours_worked = hours_worked          # Atributos de instância
        self.hour_value = hour_value
    def get_hours_workded(self):                  # Consulta
        return self.hours_worked
    def get_hour_value(self):
        return self.hour_value
    def set_hours_worked(self, new_hours_worded): # Altera
        self.hours_worked = new_hours_worded
    def set_hour_value(self, new_hour_value):
        self.hour_value = new_hour_value
    # Método obrigatório, sobrescreve o método abstrato da superclasse abstrata
    def compute_salary(self):                     # Cálculo do salário total
        return self.hours_worked * self.hour_value

