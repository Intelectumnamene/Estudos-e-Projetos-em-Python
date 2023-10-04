def meu_decorators(função):
    def wrapper():
        print('Antes')
        função()
        print('Depois')
    return wrapper
@meu_decorators

def parabenizar():
    print('Parabéns!!!')

#foi substituido pelo @meu_decorators
#resultado = meu_decorators(parabenizar)
#resultado()
parabenizar()
