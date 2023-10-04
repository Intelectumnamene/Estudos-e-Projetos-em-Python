

from datetime import datetime

def meu_decorators(horario):
    def o_que_acontece():
        print(datetime.now())
        horario()
        print(datetime.now())
    return o_que_acontece  

@meu_decorators
def horario_de_registro():
    print('Registrado!!!')

horario_de_registro()  