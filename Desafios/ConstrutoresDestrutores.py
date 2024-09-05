########## Construtores e Destrutores ##########

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instãncia da classe!")

    def falar(self):
        print("Auuuuuuu")

c = Cachorro("Chapie", "Amarelo")
c.falar()


