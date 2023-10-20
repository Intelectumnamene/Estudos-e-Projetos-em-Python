from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, numero):
        pass

    @abstractmethod
    def reduzir_claridade(self, numero):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, numero):
        return 'Aumentar claridade para {}'.format(numero)
    
    def reduzir_claridade(self, numero):
        return 'Diminuir claridade para {}'.format(numero)

monitor_fullhd = MonitorFullHD()
print(monitor_fullhd.aumentar_claridade(6))
print(monitor_fullhd.reduzir_claridade(7))
