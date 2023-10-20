class Pessoa:
    def apresentar(self, nome, idade = None, profissao = None):
        if idade and profissao != None:
            print ('{},{},{}'.format(nome, idade, profissao))
        
        elif idade != None:
            print('{},{}'.format(nome,idade))
        
        elif profissao != None:
            print('{},{}'.format(nome, profissao))
        
        else:
            print(nome)

pessoa = Pessoa()
pessoa.apresentar(nome= 'Amanda', idade = 18, profissao='Programadora')
pessoa.apresentar(nome= 'Amanda', idade = 18)
pessoa.apresentar(nome= 'Amanda', profissao='Programadora')
pessoa.apresentar(nome= 'Amanda')