import random
print (random.random())#gera um valor de 0.0 a 1.0 
#gerar um valor decimal do valor mínimo ao máximo.
print (random.uniform(4, 10))
print (random.randint(4, 10))

cores = ['verde ', 'vermelho', 'azul']#escolher opção aleatória
print(random.choice(cores))
print(random.choices(cores, k = 2))

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3', 'carta4']#Embaralhar uma lista
print(random.shuffle(cartas_de_um_baralho))
print (cartas_de_um_baralho)
