print("##########Identação e Blocos##########", end="\n\n")

def sacar(valor):
    saldo = 100
    if saldo >= valor:
        print("Valor Sacado!")
    
    print("Obrigado! Volte sempre!")

sacar(89)

print("##########Estrutura Condicionais##########", end="\n\n")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade ", idade, "você já pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Menor de idade ", idade, "você não pode tirar CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade ", idade, "você já pode tirar CNH")
else:
    print("Menor de idade ", idade, "você não pode tirar CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade ", idade, "você já pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor de idade ", idade, "você não pode tirar CNH")

print("##########Estrutura Aninhadas##########", end="\n\n")

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 5000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado con uso do cheque especial!")
    else:
        print("Saque não realizado! Saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

print("##########Estrutura Ternário##########", end="\n\n")

status = "Sucesso" if saldo <= saldo else "falha"
print(f"{status} ao realizar o saque!!")
