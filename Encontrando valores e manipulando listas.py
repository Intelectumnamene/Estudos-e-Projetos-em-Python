valores = [1,2,3,4,2,5,6,7,8,9,10]
anos = [2020, 2030, 2040,2050]

#Adicionar ao final da lista
valores.append(11)
print(valores)

# unir listas
valores.extend(anos)
print(valores)

#adicionar lista
nova_lista = valores + anos
print(nova_lista)

#inserir valores dentro de uma lista.
print( anos[1])
anos.insert(2, 2031)
print(anos)

#extrair com base no índice
anos_2020 = anos.pop(0)
print(anos_2020)
#remover intem da lista
#anos.remove(2050)
#print(anos)

del valores[1:7]
print (valores)

#contando a ocorrencia de um valor na lista
print(valores.count(2))

#resetar
valores.clear()
print(valores)