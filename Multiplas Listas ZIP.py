from itertools import zip_longest

a_lista = ['A', 'B', 'C', 'D','E']
b_lista = [1, 2, 3, 4, 5]

for a,b in zip(a_lista,b_lista):
    print(a)
    print(b)

produtos = ['produtoto 1','produtoto 2','produtoto 3','produtoto 4','produtoto 5']
precos = [250,150,220,550,50]
for a,b in zip(produtos,precos):
    print('Salvando produto{} valor R$ {}'.format(a,b))

títulos = ['Titulo 1','Titulo 2','Titulo 3','Titulo 4']
descrições = ['Descrição 1','Descrição 2','Descrição 3']

for titulo, descriçao in zip_longest(títulos,descrições):
    print ('Encontramos o {} descrição: {}'.format(titulo,descriçao)) 
