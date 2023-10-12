import os
# with open ('celulares.txt', 'w') as arquivo:
#     arquivo.write('celular 2')

# with open('nomes.txt', 'a', newline='') as arquivo:
#     arquivo.write('rafael'+ os.linesep)

#nomes = ['Lucas', 'Carol', 'Jeff', 'Douglas']

# with open('nomes.txt', 'a', newline='') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)

# numeros = [1,2,3,4,5,6]
# with open('numeros.txt', 'a', newline='') as arquivo:
#     for numero in numeros:
#         arquivo.write(str(numero) + os.linesep)

# 'w' tipo de operação = escrita
# 'a' tipo de operaçao que permite adicionar irformações sem apagar o que foi escrito antes.
# newline='' e os.linesep permite a qubra de linha sem junta as palavras
# 'r' usado domente para ler algo
# 'r+' usado para ler e escrever algo

# with open('nomes.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha)

with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('9000')



