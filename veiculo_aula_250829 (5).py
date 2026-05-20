"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema (Meet: vbc-shqr-wxd):
- Com base nos conceitos de Programação Orientada a Objetos (POO),
implemente a entidade veículo com estas características (atributos):
modelo,
ano, e
valor.

- Implemente:
1- Crie Um programa .py e a classe Veiculo
2- Crie o construtor da classe com os atributos: modelo, ano, valor
class NomeClasse:                               # Modelo
    def __init__ (self, parametro1, parametro2): # Construtor
        self.atributo1 = parametro1
        self.atributo2 = parametro2
3- No main, crie (instancie) pelo menos dois objetos da classe. Teste
if __name__ == '__main__':            # mai <tab> (tecla de atalho)
    objeto1 = NomeClasse(arg1, arg2)  # Cria (instancia) o primeiro objeto da classe
4- Crie os métodos (defs) gets dos atributos para consultar os dados.
   def get_atributo1(self):  # Modelo do método get (consulta)
       return self.atributo1
5- No main, use (teste) os métodos gets para consultar os objetos criados
   print("Msg.:", nome_objeto.nome_metodo())  # print("\nModelo:", carro1.get_modelo())
6- Crie os métodos sets (defs) dos atributos para alterar os dados.
   def set_atributo1(self, novo_valor):  # Modelo do método set (altera)
       self.atributo1 = novo_valor
7- No main, use (teste) os métodos sets para os alterar os objetos criados
   nome_objeto.nome_metodo("Novo valor")
8- Crie o método mostra_dados. Ele mostra todos os atributos da classe e não
   retorna nada. Teste

9- Crie o método (def) aumenta_valor. Ele recebe o valor do aumento em reais que
   será somado ao atributo valor do carro e atualiza o valor do carro na memória.
   Não retorna nada. Teste
10- Peça para o usuário fornecer o valor do aumento do veículo. Teste

"""


# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Veiculo(object):
# class Veiculo():                  # Três formas equivalentes de criar classe
class Veiculo:
    def __init__(self, modelo, ano, valor):  # Atalho: def _ <tab> # Construtor
        self.modelo = modelo                 # Atributos
        self.ano = ano
        self.valor = valor
    def get_modelo(self):                    # Método get (consulta)
        return self.modelo
    def get_ano(self):
        return self.ano
    def get_valor(self):
        return self.valor
    def set_modelo(self, novo_modelo):       # Método set (altera)
        self.modelo = novo_modelo
    def set_ano(self, novo_ano):
        self.ano = novo_ano
    def set_valor(self, novo_valor):       # Sem crítica
        self.valor = novo_valor
    def mostra_dados(self):                  # Solução 1, com atributos
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)
        print('Valor:', self.valor)
    def aumenta_valor(self, valor_aumento):
        self.valor = self.valor + valor_aumento
        # self.valor += valor_aumento


if __name__ == '__main__':                  # Atalho: mai <tab>
    carro1 = Veiculo('HB', 2022, 80000.00)  # chama método __init__ (construtor)
    print("Objeto carro 1:", carro1)        # Teste
    # <veiculo.Veiculo object at 0x0000024149FF6FD0>  # Endereço hexadecimal
    carro2 = Veiculo('Corolla', 2024, 190000.00)
    print("Objeto carro 2:", carro2)
    # <veiculo.Veiculo object at 0x0000024149FF6F70>
    print(carro1)
    print(type(carro1))
    retorno = carro1.get_modelo()           # Usa variável
    print("Dados do carro 1:\nModelo:", retorno)
    print("Dados do carro 1:\nModelo:", carro1.get_modelo())  # Consulta
    print("Ano:", carro1.get_ano())
    print(f"Valor: R$ {carro1.get_valor():.2f}")  # Valor com 2 casas decimais
    print("Dados do carro 2:\nModelo:", carro2.get_modelo())   # Direto no print
    print("Ano:", carro2.get_ano())
    print(f"Valor: R$ {carro2.get_valor():.2f}")
    carro1.set_modelo('HB20')    # Altera (substitui) o valor do objeto
    print("Modelo atualizado:", carro1.get_modelo())  # Confirma a alterção
    carro2.set_valor(122000.00)  # Altera (substitui) o valor do objeto
    print("Valor atualizado:", carro2.get_valor())    # Confirma a alterção
    carro1.mostra_dados()
    carro2.mostra_dados()
    carro1.aumenta_valor(1900.00)    # Passa o argumento (1900.00)
    print("Valor atualizado:", carro1.get_valor())  # Confirma
    vl_aumento = float(input("Valor aumento: "))    # vl_aumento = 22.22
    carro2.aumenta_valor(vl_aumento)            # Usuário digitou no input
    print("Valor atualizado com input:", carro2.get_valor())  # Confirma
