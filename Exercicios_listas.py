# =========================================================
# LISTA DE EXERCÍCIOS RESOLVIDA — PYTHON (LISTAS)
# =========================================================

# ---------------------------------------------------------
# EXERCÍCIO 1
# Criando uma lista
# ---------------------------------------------------------

# Criando uma lista com nomes
nomes = ["Rafael", "Ana", "Caio", "Lucas", "Maria"]

# Exibindo a lista
print("Exercício 1")
print(nomes)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 2
# Acessando elementos da lista
# ---------------------------------------------------------

# Mostrando o primeiro elemento
print("Exercício 2")
print("Primeiro nome:", nomes[0])

# Mostrando o último elemento
print("Último nome:", nomes[-1])

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 3
# Adicionando elementos com append()
# ---------------------------------------------------------

nomes2 = ["Rafael", "Ana", "Caio"]

# Adicionando um novo elemento no final
nomes2.append("Carlos")

print("Exercício 3")
print(nomes2)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 4
# Inserindo elemento em posição específica
# ---------------------------------------------------------

nomes3 = ["Rafael", "Ana", "Caio"]

# Inserindo "Pedro" na posição 1
nomes3.insert(1, "Pedro")

print("Exercício 4")
print(nomes3)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 5
# Removendo elementos pelo valor
# ---------------------------------------------------------

nomes4 = ["Rafael", "Ana", "Caio"]

# Remove o valor "Ana"
nomes4.remove("Ana")

print("Exercício 5")
print(nomes4)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 6
# Removendo elementos pelo índice
# ---------------------------------------------------------

numeros = [10, 20, 30, 40]

# Remove o elemento da posição 2
numeros.pop(2)

print("Exercício 6")
print(numeros)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 7
# Descobrindo tamanho da lista
# ---------------------------------------------------------

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

# len() retorna o tamanho da lista
print("Exercício 7")
print("Quantidade de frutas:", len(frutas))

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 8
# Percorrendo lista com FOR
# ---------------------------------------------------------

frutas2 = ["Maçã", "Banana", "Uva"]

print("Exercício 8")

# Percorrendo cada item da lista
for fruta in frutas2:
    print(fruta)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 9
# Soma dos elementos da lista
# ---------------------------------------------------------

numeros2 = [10, 20, 30, 40]

# sum() soma todos os valores
soma = sum(numeros2)

print("Exercício 9")
print("Soma =", soma)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 10
# Maior e menor valor
# ---------------------------------------------------------

numeros3 = [5, 2, 9, 1, 7]

print("Exercício 10")

# max() retorna o maior valor
print("Maior número:", max(numeros3))

# min() retorna o menor valor
print("Menor número:", min(numeros3))

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 11
# Ordenando lista crescente
# ---------------------------------------------------------

numeros4 = [5, 2, 9, 1, 7]

# sort() ordena a lista
numeros4.sort()

print("Exercício 11")
print(numeros4)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 12
# Ordenando lista decrescente
# ---------------------------------------------------------

numeros5 = [5, 2, 9, 1, 7]

# reverse=True faz ordem decrescente
numeros5.sort(reverse=True)

print("Exercício 12")
print(numeros5)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 13
# Verificando se elemento existe
# ---------------------------------------------------------

linguagens = ["Java", "Python", "C++"]

print("Exercício 13")

# Verificando se "Python" está na lista
if "Python" in linguagens:
    print("Python existe na lista")
else:
    print("Python não existe")

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 14
# Copiando listas
# ---------------------------------------------------------

lista1 = [1, 2, 3]

# copy() cria uma cópia da lista
lista2 = lista1.copy()

print("Exercício 14")
print(lista2)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 15
# Criando lista de números pares
# ---------------------------------------------------------

pares = []

# range(1,21) gera números de 1 até 20
for i in range(1, 21):

    # Verificando se o número é par
    if i % 2 == 0:
        pares.append(i)

print("Exercício 15")
print(pares)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 16
# List Comprehension
# ---------------------------------------------------------

# Criando lista de pares de forma reduzida
pares2 = [i for i in range(1, 21) if i % 2 == 0]

print("Exercício 16")
print(pares2)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 17
# Média dos valores
# ---------------------------------------------------------

notas = [7, 8, 9, 10]

# Calculando média
media = sum(notas) / len(notas)

print("Exercício 17")
print("Média =", media)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 18
# Contando elementos repetidos
# ---------------------------------------------------------

numeros6 = [5, 1, 5, 3, 5, 7]

print("Exercício 18")

# count() conta quantas vezes aparece
print("Quantidade de 5:", numeros6.count(5))

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 19
# Invertendo lista
# ---------------------------------------------------------

numeros7 = [1, 2, 3, 4]

# reverse() inverte a lista
numeros7.reverse()

print("Exercício 19")
print(numeros7)

print("\n")


# ---------------------------------------------------------
# EXERCÍCIO 20
# Matrizes (lista dentro de lista)
# ---------------------------------------------------------

# Criando matriz 2x2
matriz = [
    [1, 2],
    [3, 4]
]

print("Exercício 20")

# Acessando elementos específicos
print("Elemento [0][0]:", matriz[0][0])
print("Elemento [1][1]:", matriz[1][1])

print("\n")


# =========================================================
# FIM DA LISTA
# =========================================================