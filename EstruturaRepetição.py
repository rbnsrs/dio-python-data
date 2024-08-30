print("##########Estrutura de Repetição##########", end="\n\n")

#Exemplo com Iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
    else:
        print()
    

#Exemplo utilizando a função built-in range
for numero in range(0, 21, 2):
    print(numero, end=" ")

# Estrutura com While

print("\nEstrutura com While", end="\n\n")
opcao = -1 

while opcao != 0:

    opcao = int(input("Esolha uma opção: \n[1] Sacar \n[2] Extrato \n[3] Saldo \n[0] Sair\n\nNº: "))
                      
    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Extrato")
    elif opcao == 3:
        print("Saldo")
else:
    print("Obrigado por usar o sistema, bye!")

print("\nOutro While", end="\n\n\n")

while True:
    numero = int(input("Digite um número: "))

    if numero == 10:
        print("\n\nSaindo pela esquerda")
        break

    print(numero)