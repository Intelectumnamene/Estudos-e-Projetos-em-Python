import  random
escolha = input('Escolha cara ou coroa :')
sorteio = ['cara', 'coroa']
resultado= random.choice(sorteio)
print('Você escolheu {}. Foi sorteado {} : Obrigado!'.format( escolha, resultado))

nomes = ['Pedro', 'Gisele', 'Maria', 'Gabriela', 'Rita']
#escolha = input("Escolha entre esses 5 nomes: 'Pedro', 'Gisele', 'Maria', 'Gabriela', 'Rita'")
resultado = random.choice(nomes)
print("O(a) sorteado(a) foi {} : ".format(resultado))

print(random.randint(10, 100))