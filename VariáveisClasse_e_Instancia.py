############# Variáveis de Classe e de Instância

class Estudante:
    escola = "Dio"

    def __init__(self, nome, matricula):
        self.nome = nome 
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostar_valores(*objs):
    for obj in objs:
        print(obj)
    

aluno1 = Estudante("Santos", 5571)
aluno2 = Estudante("Peixei", 5005)
mostar_valores(aluno1, aluno2)

Estudante.escola = "Python"
aluno3 = Estudante("Chappie", 3003)
mostar_valores(aluno1, aluno2, aluno3)

################### Métodos de Classe e Métodos Estático

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Santos", 100)
print(p.nome, p.idade)

p = Pessoa.criar_data_nascimento(1979, 3, 28, "Epaminondas")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(15))


############################# Interfaces -> Abastratas (Em Python)
# Definem o que uma classe deve fazer, um padrão que as classes que implementarem, devem fazer. "Um Molde."
# Definir um contrato - o que deve se feito. Classes abstratas não podem ser instânciadas.

# Abastract Basic Class (ABC) - Módulo que fornece classes abastratas. Por padrão, Python não tem classe abastrata.
from abc import ABC, abstractmethod


class ControlRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControlRemoto):
    def ligar(self):
        print("Ligando a TV ...")
        print("Ligado!")

    def desligar(self):
        print("Desligando a TV ...")
        print("Desligado!")


class ControleArCondicionado(ControlRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado ...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o ar Condicionado ...")
        print("Desligado!")

controle = ControleTV()
controle.ligar()
controle.desligar()


controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.desligar()