class CPU:
    def processar(self):
        print("CPU processando")

class Monitor:
    def mostrar(self):
        print("Mostrando na tela")

class Computador:
    def __init__(self):
        self.cpu = CPU()
        self.monitor = Monitor()

    def ligar(self):
        self.cpu.processar()
        self.monitor.mostrar()

meu_computador = Computador()
meu_computador.ligar()

class Passageiro:
    def __init__(self, nome):
        self.nome = nome

class Voo:
    def __init__(self, numero):
        self.numero = numero

class Reserva:
    def __init__(self, passageiro, voo):
        self.passageiro = passageiro
        self.voo = voo

    def mostrar_detalhes(self):
        print(f"Reserva de {self.passageiro.nome} para o voo {self.voo.numero}")

passageiro1 = Passageiro("João")
voo1 = Voo("XY123")
reserva1 = Reserva(passageiro1, voo1)
reserva1.mostrar_detalhes()