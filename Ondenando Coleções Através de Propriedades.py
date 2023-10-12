from operator import itemgetter

# nomes = [ 'Zack', 'Camilla', 'Julius', 'Romer']
# valores = [31,23,36,21,33,37,7,20,23]
# pessoas = [{'nome': 'John', 'idade': 32, 'nivel_acesso': 2},
#            {'nome': 'Carol', 'idade':18, 'nivel_acesso': 3},
#            {'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5},
#            {'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1},]

# pessoas.sort(key=itemgetter('nome'))
# print(pessoas)


# produtos = [('Celular',750), ('Bicicleta',1500),('Microfone',550)]

# produtos.sort(key=itemgetter(0),reverse=True)
# print(produtos)

matriz = [[5,10],[15,21],[1,5]]
matriz.sort(key=itemgetter(1))
print(matriz)