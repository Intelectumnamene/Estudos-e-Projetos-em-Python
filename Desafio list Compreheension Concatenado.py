from pprint import pprint

def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0 :
        return True
    else: 
        return False
pprint(list(i for i in range (1,11)if eh_numero_par(i)))

cores = ['vermelho', 'azul', 'verde','amarelo', 'rosa', 'preto']
pprint([str(cores.index(cor)+1) + '-'+ cor for cor in cores])



participantes = ['Joel', 'Jessica', 'Maria', 'Cris', 'Larissa','Rafael', 'Marcus', 
                  'John']
pagamento_realizado = ['Joel', 'Jessica', 'Maria', 'Cris']
pprint([i + ' PAGO' if i in pagamento_realizado else i + ' Devendo' for i in 
        participantes]) 