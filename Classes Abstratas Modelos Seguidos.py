#Criar um contrato(esqueleto) que deve ser implementado na classe que a herda.
#Obriga que certas propriedades sejam implementadas dentro de uma classe.

from abc import ABC, abstractmethod

class Camera (ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print('Alterar a lente para {}'.format(tamanho))

camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)