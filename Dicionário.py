# pessoa
#     nome
#     Idade
#     altura

pessoa = ['Luiz',18, 1.60, 'Mike', 50,1.80]

#Dicionário (chave,valor)

dicionario_pessoa = {'nome': 'Luiz','idade':41, 'altura': 1.60}
pessoa_2 = dict(nome = 'Luiz', idade = 41, altura = 1.60)

#Acessando diferentes propriedades de um dicionário

# print(dicionario_pessoa.keys())#apenas chaves
# print(dicionario_pessoa.values())#apenas valores
# print(dicionario_pessoa.items())#par de chave e valores

#iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])