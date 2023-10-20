class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        self.habilidade = ['Habilidade 1', 'Habilidade 2', 'Habilidade 3']
    #Represenatção para programadores(chamado com método repr(pessoa))

    def __repr__(self):
        return 'Classe pessoa com propriedade nome e habilidade'
    #O que deve ser mensurado para determinar a quantidade daquela classe (chamada com método(len(pessoa)))
    def __len__(self):
        #len(pessoa)?
        return len(self.habilidade)
    def __str__(self):

        return '{} com as habilidades {}'.format(self.nome,self.habilidade)
    

pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(len(pessoa))
print(pessoa)
print(dir(pessoa))