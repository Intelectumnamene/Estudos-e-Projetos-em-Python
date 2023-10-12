numeros = [2,2,5,8]
frutas = {'maça','uva','banana','maça','morando',}
#convertendo para sets
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

#adicionar novos valores
set_numeros.add(10)
print(set_numeros)

#conjuntos
numeros1 = [2,2,5,8]
numeros2 = [2,2,3,5,8]
a = set(numeros1)
b = set(numeros2)
print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))
