from datetime import datetime
import random

print("Registro de usuário.")

nome = input("Informe o seu nome :")
idade = int(input("Informe sua idade :"))
data_de_aniversário = input("Por favor! Informe sua data de aniversário. Exemplo: dd/mm/ano : ")
print(data_de_aniversário)
data_de_registro = print(datetime.today())
cartoes = ['R$50,00','R$250,00','R$120,00']
sorteio = random.choice(cartoes)
print("Olá {}! Seu registro foi conluído com sucesso no dia {}.".format(nome, datetime.today()))
print("Hove um sorteio e você ganhou um cartão de comprar no valor de {} : ".format(sorteio) )
