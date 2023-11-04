numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

#Map

nomes = ['Luiz', 'Gisele', 'Pedro', 'John']
def aprovar_pessoa(nome):
    return nome + ' - APROVADO'
print(list(map(aprovar_pessoa, nomes)))

nova_lista = [2 * i for i in range(10)]
print(nova_lista)


nomes1 = ['Luiz', 'Gisele', 'Pedro', 'John']
#print([nome + ' Aprovado' for nome in nomes1])
print([aprovar_pessoa(nome)for nome in nomes1])