menu = '''
###############################################
#############  Escolha uma Opção  #############
#    [1] - Depositar                          # 
#    [2] - Sacar                              #  
#    [3] - Saldo                              #
#    [4] - Extrato                            #
#    [0] - Sair                               #
#                                             #  
###############################################
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

def depositar(valor):
    if valor > 0:
       
        global saldo
        saldo += valor
        
        global extrato
        extrato += f"Depósito: R$ {valor: .2f}\n"
   
    else:
        print("Operação falhou! Valor informado deve ser maior que zero!")

def sacar(valor):
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUE

    if valor > saldo:
        print("Sem chance! Você não tem saldo suficiente")
    
    elif valor > limite:
        print("Sem chance! Seu limite de saque não é esse!")
    
    elif numero_saques >= LIMITE_SAQUE:
        print("Sem chance! Você já sacou o quanto podia!")

    elif valor > 0 and valor <= saldo:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("Operação inválida! Valor informado é inválido")

def mostrar_extrato():
    global saldo, extrato
    print("\n====================  Extrato    ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSeu Saldo é de: R$ {saldo:.2f}")
    print("=======================================================")

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))
        depositar(valor)

    elif opcao == "2":
        valor = float(input("Informe  valor do saque: "))
        sacar(valor)

    elif opcao == "3":
        print(f"\nSeu saldo é de: R$ {saldo:.2f}")
    
    elif opcao == "4":
        mostrar_extrato()
    
    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor, selecione uma operação novamente")