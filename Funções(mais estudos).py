def pai (numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filhor 2')
    if numero == 1 :
        return filho_2 
    else:
        return filho_1
resultado = pai(2)
resultado()