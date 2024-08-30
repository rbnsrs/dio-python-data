######### Funções em Python #########
print("\n####Funções em Python####", end ="\n\n")

def exibir_mensagem():
    print("Olá Mundo!!")

def exibir_mensagem_2(nome):
    print(f"Olá Mundo!! Seja bem vindo {nome}!")

def exibir_mensagem_3(nome = "Antonio"):
    print(f"Olá Mundo!! Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome = "Santos")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Chappie")

print("\n####Retorno em Funções Python####", end ="\n\n")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero + 1

    return antecessor, sucessor

print("O valor da soma é:", calcular_total([10, 20, 30, 4]))
print("O antecessor e sucessor são:", retorna_antecessor_e_sucessor(10))

print("\n####Funções Python - Argumento Posicionais e Nomeados####", end ="\n\n")

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca ="Volks", modelo="Fusca", ano=2024, placa="DEC-1324")
salvar_carro(**{"marca": "Fiat", "modelo": "Celta", "ano": 1999, "placa": "FGH-5678"})

print("\n####Funções Python - Args e Kwargs####", end ="\n\n")

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n" .join(args)
    meta_dados = "\n" .join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 29 de agosto de 2024",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one—and preferably only one—obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea—let's do more of those!",
    autor = "Tim Petters",
    ano = 1999,
    )

print("\n####Funções Python - Argumentos por posição####", end ="\n\n")

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

print("\n####Funções Python - Argumentos somente nomeados####", end ="\n\n")

def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_2(modelo="Palio", ano=1985, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

print("\n####Funções Python - Argumentos por nome e posição####", end ="\n\n")

def criar_carro_3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_3("Palio", 1998, "ABC-1235", marca="Fiat", motor="1.0", combustivel="Gasosa")

print(
      '''#######################################
         # Chamando função em função           #  
         #######################################
      ''') 
def somar(a, b):
    return print("O resultado da soma é: ", a + b)
def subtrair(a, b):
    return print("O resultado da subtração é: ", a - b)
def multiplicar(a, b):
    return print("O resultado da multiplicação é: ", a * b)
def divdir(a, b):
    return print("O resultado da divisão é: ", a / b)

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
      
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, divdir)
exibir_resultado(10, 10, multiplicar)