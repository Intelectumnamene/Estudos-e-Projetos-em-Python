class Carro:
    def ligar(self):
        print('Ligando Carro')
    
class Moto: 
    def ligar(self):
        print('Ligando Moto')

def iniciar(veículo):
    veículo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)