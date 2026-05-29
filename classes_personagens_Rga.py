# 1. Classe Base
class Personagem:
    def __init__(self, nome, nivel=1):
        self.nome = nome
        self.nivel = nivel
        self.vida = 100

    def atacar(self):
        return f"{self.nome} realizou um ataque básico."

# 2. Classe Guerreiro (Herança)
class Guerreiro(Personagem):
    def usar_espada(self):
        return f"{self.nome} desferiu um golpe pesado com a espada!"

# 3. Classe Mago (Herança)
class Mago(Personagem):
    def lancar_magia(self):
        return f"{self.nome} conjurou uma bola de fogo!"

# 4. Classe Arqueiro (Herança)
class Arqueiro(Personagem):
    def atirar_flecha(self):
        return f"{self.nome} disparou uma flecha certeira!"

# 5. Classe Ladino (Herança)
class Ladino(Personagem):
    def furtividade(self):
        return f"{self.nome} desapareceu nas sombras."

# 6. Classe Clerigo (Herança)
class Clerigo(Personagem):
    def curar(self):
        return f"{self.nome} canalizou energia sagrada para curar o grupo."

# 7. Classe Necromante (Herança de Mago)
class Necromante(Mago):
    def reviver_esqueleto(self):
        return f"{self.nome} invocou um lacaio esqueleto do submundo."

# 8. Classe Paladino (Herança de Guerreiro)
class Paladino(Guerreiro):
    def escudo_divino(self):
        return f"{self.nome} ativou uma barreira de luz protetora."


# --- Testando o Cenário 1 ---
heroi1 = Paladino("Arthur")
heroi2 = Necromante("Malazar")

print(heroi1.usar_espada())    # Herda de Guerreiro
print(heroi1.escudo_divino())  # Próprio de Paladino
print(heroi2.lancar_magia())   # Herda de Mago
print(heroi2.reviver_esqueleto()) # Próprio de Necromante