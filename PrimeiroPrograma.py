#Primeiro Programa - Python
print("oi, seja bem vindo")

#Tipos de dados - Informa o quanto de memória será usado.
print(1 + 10)
print(1.5 + 5.8)
bool(True)
print(False)
print("Python", """Python""", 'Python', 'Python')

#Modo interativo - Executar comandos rápidos e ver resultados rápidos.
#Módulo help - Lista todos os módulos/métodos do python. Podemos buscar por um objeto específico.
#Python procura se usar o padrão snake_case. Ex: exemplo_de_nome

#Conversão de tipos
#Algumas vezes precisamos converter valores de variáveis para executar uma determinada ação.

print("########Convertendo Variáveis###########")
print(int(1.99999))
print(int("10"))
print(float("10.10"))

#Funções de Entrada e saída. Input é uma função bultin, recebe um valor e transforma em string, independente do valor digitado.

nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")

