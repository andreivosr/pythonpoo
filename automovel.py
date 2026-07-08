
from random import randint
from time import sleep

VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75

VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1

class Automovel:
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valorFatura = 0
        self.nomeCliente = ""

    def alugar(self, nomeCliente):
        self.alugado = True
        self.nomeCliente = nomeCliente
        print(f"O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nomeCliente}")


    def devolver_automovel(self):
        self.alugado = False
        print(f"O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nomeCliente}")
        self.nomeCliente = ""

    def gerar_valor_fatura(self, numeroDePedagios, QuilometrosRodados):
        raise NotImplementedError

class Carro(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um carro")


    def gerar_valor_fatura(self, numeroDePedagios, QuilometrosRodados):
        self.valorFatura = numeroDePedagios * VALOR_PEDAGIO_CARRO + QuilometrosRodados * VALOR_KM_RODADO_CARRO
        print(f"Fatura do carro {self.montadora} {self.modelo} foi R${self.valorFatura}")

class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O automóvel adquirido foi um carro")

        
    def gerar_valor_fatura(self, numeroDePedagios, QuilometrosRodados):
        self.valorFatura = numeroDePedagios * VALOR_PEDAGIO_MOTO + QuilometrosRodados * VALOR_KM_RODADO_MOTO
        print(f"Fatura do carro {self.montadora} {self.modelo} foi R${self.valorFatura}")


#--------------------------------------------

fiesta = Carro("Ford", "Fiesta", False)
fiesta.alugar("João")

sleep(randint(7, 10))



