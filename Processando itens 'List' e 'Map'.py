numeros = []
for i in range (5):
    numeros.append(i)
print(numeros)


nomes = ['Larissa' , 'Rafael' , 'Marcos' , 'john']
def aprovar_pessoas(nome):
    return nome + ' = Aprovado'
print(list(map(aprovar_pessoas, nomes)))
