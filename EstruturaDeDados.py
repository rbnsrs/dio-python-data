################ Estrutura de Dados ################

print("############## Declarando Listas ##############")

frutas = ["Laranja", "Maça", "Uva"]
print(frutas)
print("###############################################")

frutas = []
print(frutas)
print("###############################################")

letras = list("Python")
print(letras)
print("$$$$$$ Fatiamento de lista $$$$$$")
print("letras[2:]: ",letras[2:])
print("letras[:2]: ", letras[:2])
print("letras[1:3] : ", letras[1:3])
print("letras[0:3:2]: ", letras[0:3:2])
print("letras[::]: ", letras[::])
print("letras[::-1]: ", letras[::-1])
print("###############################################")

numeros = list(range(10))
print(numeros)
print("###############################################")

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

print("Iterar Listas")
for carro in carro:
    print(carro)
print("###############################################")

numeros = [11, 20, 30, 44, 9, 65, 34, 50, 81, 89]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
print("###############################################")

print("########## List comprehension ##########")

pares2 = [numero for numero in numeros if numero %2 ==0]
print(pares2)

print("###############################################")
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print("Quadrado: ", quadrado)

#List comprehension
cubo = [numero **3 for numero in numeros]
print("Cubo: ", cubo)



print("#####################Métodos da Lista##########################")

lista = [1, "Python", [40, 30, 20]]
l2 = lista.copy()
print(id(lista), id(l2))
