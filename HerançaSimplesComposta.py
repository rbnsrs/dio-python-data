########################## Herança Simples e Composta ##########################

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor 
        self.placa = placa 
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando Motor")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Motocicleta("Preto", "ABC-1234", 2)
print("Ligando motor Moto: " ), moto.ligar_motor()

carro = Carro("Azul", "XDE-0009", 4)
print("Ligando motor Carro: "), carro.ligar_motor()

caminhao = Caminhao("Roxo", "EHE-0329", 8)
print("Ligando motor Caminhão: ") ,caminhao.ligar_motor()


################## Herança Multipla ##################

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
   
    def __str__(self):
        return f"{self.__class__.__name__}: {' , '.join
        ([f'{chave}={valor}' for chave, valor in self. 
        __dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "Olá! Eu estou falando!"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, nro_patas, cor_bico):
        super().__init__(cor_pelo = cor_pelo, cor_bico=cor_bico, 
        nro_patas = nro_patas)


########### Instâncias

gato = Gato(nro_patas = 4, cor_pelo = "Pardo")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="Roxo", cor_bico="Azul")
print(ornitorrinco)