class SingletonInstancia:
    _instance = None  # Armazena a única instância da classe

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Cria a instância chamando o __new__ da classe mãe (object)
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, valor):
        # Cuidado: o __init__ sempre será chamado após o __new__
        self.valor = valor

# Testando o comportamento
obj1 = SingletonInstancia("Primeiro")
obj2 = SingletonInstancia("Segundo")

print(obj1 is obj2)  # True (são exatamente o mesmo objeto na memória)
print(obj1.valor)    # "Segundo" (o segundo __init__ sobrescreveu o valor)


class Base:
    def quem_sou_eu(self):
        print("Sou a classe Base")

class Esquerda(Base):
    def quem_sou_eu(self):
        print("Entrei na Esquerda")
        super().quem_sou_eu()

class Direita(Base):
    def quem_sou_eu(self):
        print("Entrei na Direita")
        super().quem_sou_eu()

class Filho(Esquerda, Direita):
    def quem_sou_eu(self):
        print("Entrei no Filho")
        super().quem_sou_eu()

# Instanciando e chamando o método
f = Filho()
f.quem_sou_eu()

# Para visualizar a ordem exata de resolução:
print([cls.__name__ for cls in Filho.__mro__])