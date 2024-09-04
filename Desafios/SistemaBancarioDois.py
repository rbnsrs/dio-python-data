def menu():
    menu = '''\n
    ===============================================
    =============  Escolha uma Opção  =============
    *    [1] - Depositar                          * 
    *    [2] - Sacar                              *  
    *    [3] - Saldo                              *
    *    [4] - Extrato                            *
    *    [5] - Novo Usuário                       * 
    *    [6] - Nova conta                         *
    *    [7] - Listas contas                      *
    *    [0] - Sair                               *
    *                                             *  
    ===============================================
    => '''
    #return input(textwrap.dedent(menu))
    return input(menu)


def depositar(valor):
    if valor > 0:
       
        global saldo
        saldo += valor
        
        global extrato
        extrato += f"Depósito:\t\t R$ {valor: .2f}\n"
        print("\n(*_~) Depósito realizado com sucesso (*_~)")
    else:
        print("\n(-(-(-(-_-)-)-)-) Operação falhou! Valor informado deve ser maior que zero (-(-(-(-_-)-)-)-)")

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
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("(~_*) Saque realizado com sucesso (~_*)")
    
    else:
        print("(-(-(-(-_-)-)-)-) Operação inválida! Valor informado é inválido (-(-(-(-_-)-)-)-)")

def mostrar_extrato():
    global saldo, extrato

    print("\n====================  Extrato    ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSeu Saldo é de:\t\t R$ {saldo:.2f}")
    print("=======================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF §§ Somente Números §§ : ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n(-(-(-_-)-)-) Já existe usuário com esse CPF! (-(-(-_-)-)-)")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaa): ")
    endereco = input("Informe o endereço (logrdouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\n(*_~) Usuário criado com sucesso (*_~)")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n(*_~) Conta criada com sucesso (*_~)")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n(-(-(-_-)-)-) Usuário não encontrato, a conta não foi criada (-(-(-_-)-)-)")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
    
        opcao = menu()

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
        
        elif opcao == "5": 
            criar_usuario(usuarios)
        
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "7":
            listar_contas(contas)
        
        elif opcao == "0":
            print("\n(-(-(-(-(-(-(-_-)-)-)-)-)-)-)")
            print("\nSistema Finalizado - Produção Skynet")
            print("\n(-(-(-(-(-(-(-_-)-)-)-)-)-)-)\n\n")
            break

        else:
            print("Opção inválida, por favor, selecione uma operação novamente")
main()
