#Criando uma Classe

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 

    def buzina(self):
        print("Bibibibibib")
    
    def parar(self):
        print("Freando a bicicleta")
        print("Bicicleta Parou")
    
    def correr(sefl):
        print("Vrummmmmmmmmmmm")

    #def __str__ (self):
     #   return f"Bicicleta: cor{self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__ (self):
        return f"\n\n{self.__class__.__name__}: {' , '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}\n\n"
    

# Criando um obj, instância.
#b1 = Bicicleta("Azul", "Barra Forte", 2022, 600)
#b1.buzina()
#b1.parar()
#b1.correr()
#print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 39209)
print(b2)



    
