class Computador:
    def __init__(self, marca, memoria_ram,placa_de_video):
        self.marca =marca
        self.memoria_ram =memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando o computador')

    def desligar(self):
        print('Estou desligando')

    def exibir_dados_do_computador(self):
        print('Computador da marca {}, com {} de memória ram e que usa a placa de vídeo {}'
              .format(self.marca, self.memoria_ram, self.placa_de_video))
        
computardor1 = Computador ('Asus', '32gb','Nvidia')
computardor1.ligar()
computardor1.desligar()
computardor1.exibir_dados_do_computador()
computardor2 = Computador('Dell','8gb','Nvidia')
computardor2.ligar() 
computardor2.desligar()
computardor2.exibir_dados_do_computador()
