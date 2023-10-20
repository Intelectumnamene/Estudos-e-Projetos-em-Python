class Computador():
    sistema_operacional = 'Windows 10'
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video 
    def exibir_dados_do_computado(self):
        print(self.marca,self.memoria_ram,self.placa_de_video)
    
    @classmethod
    def computador_escritório(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Baixo Custo')
    
    @classmethod
    def computador_configuracao_pesado(cls,memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Vídeo - Alto Nível')
    
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False
    

computador1 = Computador.computador_escritório('8gb')
computador2 = Computador.computador_configuracao_pesado('16gb')
computador1.exibir_dados_do_computado()
print('#####')
computador2.exibir_dados_do_computado()