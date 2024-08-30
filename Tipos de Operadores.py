#Tipos de Operadores

produto_1 = 100
produto_2 = 22

print ("Soma")
print (produto_1 + produto_2)
print ("Subtração")
print (produto_1 - produto_2 + 3.5)
print ("Multiplicação")
print (produto_1 * produto_2)
print ("Divisão com Decimal")
print (produto_1 / produto_2)
print ("Divisão com Exata")
print (produto_1 // produto_2)
print ("Exponenciação")
print (2 ** 4)


print("#######Operadores de comparação########",end="\n\n")

saldo = 450
saque = 200

print("Operador de igualdade")
print ("Saldo é igual a saque ?", saldo == saque)
print("Operador de Maior")
print ("Saldo é maior que saque ?",saldo > saque)
print("Operador de Maior ou Igual")
print ("Saldo é menor ou igual saque ?",saldo >= saque)
print("Operador de Menor")
print ("Saldo é maior que saque ?",saldo < saque)
print("Operador de Menor Igual")
print ("Saldo é igual saque ?",saldo <= saque)
print("Operador de Diferente")
print ("Saldo é diferente de saque ?", saldo != saque)

print("#######Operadores de Atribuição########",end="\n\n")

#Atribuição Simples
saldo = 450
saque = 200
limite = 500

print(saldo)
#Atribuição com adição
saldo += 200
print(saldo)

saldo /= 5
print(saldo)
saldo //= 5
print(saldo)
saldo **= 5
print(saldo)
saldo %= 5

print("#######Operadores Lógicos########",end="\n\n")

exp = saldo >= saque and saque <= limite
print(exp)
exp2 = (saldo >= saque and saque <= limite) or (saldo >= saque and saque >= limite)

print(exp2)

print("#######Operadores De Identidade########",end="\n\n")
saldo = 1000
limite = 500
print(saldo is limite)
print(saldo is not limite)

print("#######Operadores De Associação########",end="\n\n")

curso = "Curso de python"
frutas = ["laranja", "Uva", "banana"]
saques = [1500, 100]

print("Python" in curso)
print("maça" not in frutas)
print(1500 in saques)










