class Computador:
    sistema_operacional = 'Windows 10'
    def __init__(self, marca, memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def ligar(self):
        print('desligar computador')

    
    def caracteristicas_computador(self):
        print('Seu computador possui a marca {}, memória ram {}, placa de video {}'.
              format(self.marca,self.memoria_ram,self.placa_de_video))
    

#print(Computador.sistema_operacional)
Computador.sistema_operacional = 'Linux'
computador = Computador('Dell','8gb','NVIDIA')
computador.marca = 'Asus'
print(computador.marca)
print(computador.sistema_operacional)
computador.caracteristicas_computador()

Computador.sistema_operacional = 'Mac'
computador2 = Computador('ASUS', '2gb', 'ATI')
print(computador2.sistema_operacional)
print(computador2.marca)
computador2.caracteristicas_computador()