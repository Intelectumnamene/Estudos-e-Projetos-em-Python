class Carro :
    def __init__(self,marca, portas, cor):
        self.marca = marca
        self.portas = portas
        self.cor = cor
    
    def dados_do_carro(self):
        print('Seu carro possui a marca {}, {} portas ,cor {}. '
            .format(self.marca,self.portas,self.cor))
        
  
meu_carro = Carro('fiat', 4 , 'Azul')
meu_carro.dados_do_carro()

meu_carro2 = Carro('Gol',2,'Marelo')
meu_carro2.dados_do_carro()

    
    # Definição da classe
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

# Criação de uma instância da classe
meu_retangulo = Retangulo(5, 3)

# Chamada de um método na instância
area = meu_retangulo.calcular_area()
print("A área do retângulo é:", area)
