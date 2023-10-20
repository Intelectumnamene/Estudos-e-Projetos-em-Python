class Pessoa:
    nome = 'Sou uma pessoa'

    def convidar(self):
        print('Olá sou uma pesssoa, vamos ao evento?')

class Profissinal:
    nome = 'Sou um profissional'

    def convidar(self):
        print('Olá sou um profissional, vamos ao evento?')

class AtorProfissional(Pessoa,Profissinal):
    pass

ator_profissional = AtorProfissional()
ator_profissional.convidar()
print(AtorProfissional.mro())

#Este exemplo mostra que nem sempre herança múltipla é a melhor opção!
#O MRO mostra isso!
#Pesquise o que é MRo em Python.