from pprint import pprint
pprint([[i for i in range (1,6)]for x in range (5)])

def aprovar_pessoa(nome):
    return nome + ' - APROVADO'
#print(list(map(aprovar_pessoa, nomes)))

nomes = ['Luiz', 'Gisele', 'Pedro', 'John']
print([aprovar_pessoa(nome)for nome in nomes if nome != 'John'])

print([i for i in range(20) if i not in (1,5,15,19)])

# def eh_numero_par(numero):
#    valor = numero % 2
#    if valor == 0:
#        return True
#    else:
#        return False
# print([i for i in range(20) if eh_numero_par(i)])

participantes = ['Luiz', 'Gisele', 'Pedro', 'John']
ganhadores = ['Gisele', 'Pedro']

print([i + ' GANHADOR' if i in ganhadores else i + ' NÃO SELECIONADO' for i in participantes])