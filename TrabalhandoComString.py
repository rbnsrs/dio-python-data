# Métodos da Classe string #

nome = "Santos Campeão"

print(nome.upper())
print(nome.lower())
print(nome.title())

print("\n Eliminando Espaços\n")

name = "    Olá mundo!   "
print(name + ".")
print(name.strip() + ".")  #Remove todos os espaços
print(name.lstrip() + ".") #Remove os espaços da esquerda
print(name.rstrip() + ".") #Remove os espaços da direita


print("\n Junção e Centralização\n")

texto = "Python"

print("####" + texto + "####")
print(texto.center(14))
print(texto.center(14, "#"))
print("-".join(texto))

print("####\n Interpolação de variáveis \n####")

nome = "Santastico"
idade = 100
profissao = "Timasso"
linguagem = "Arte"
saldo = 3.1415161818
dados = {"Nome": "Guilherme", "Idade": 28}

print("Olá, me chama %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso"
      "de %s." %(nome, idade, profissao, linguagem))

print("Nome %s idade %d" %(nome, idade))
print()
print("Nome: {} idade: {}" .format(idade, nome))
print()
print("Nome: {1} Idade: {0}" .format(idade, nome))
print()
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))
print()
print("Nome: {Nome} Idade: {Idade}" .format(**dados))
print()
print(f"Nome: {nome} Idade: {idade}")
print()
print(f"Saldo: {saldo:2.2f}")
print()


print("\n Fatiamento de String \n")

nome = "Santos Santastico Campeão"

print(nome[0])
print(nome[:5])
print(nome[6:])
print(nome[8:11])
print(nome[4:10:1])
print(nome[:])
print(nome[:: -1])

print("\n String Multiplas Linhas \n")

nome = "Jim Morrison"

mensagem = f'''
Olá! Venho dizer que quando as portas da perpecpção
estiverem realmente abertas, você {nome}, poderá
ver as coisas como realmente são'''
print(mensagem)

