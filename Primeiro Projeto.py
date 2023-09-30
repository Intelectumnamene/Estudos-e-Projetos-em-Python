from datetime import datetime
import random

print("Seja bem-vindo a nossa empresa!")

nome = input("Informe o seu nome :")
idade = int(input("Informe sua idade :"))
aniversario = datetime.strptime( input('Digite sua data de aniversário no formato dd/mm/aaaa: '), '%d/%m/%Y')
data_cadastro = datetime.today()
cartoes = ['R$50,00','R$250,00','R$120,00']
sorteio = random.choice(cartoes)
print("Olá {} seu registro foi concluído no dia {}/{}/{}.".format(nome,data_cadastro.day,data_cadastro.month,data_cadastro.year))
print("Você aca ba de ser contemplado com um cartão no valor de : {} ".format(sorteio))