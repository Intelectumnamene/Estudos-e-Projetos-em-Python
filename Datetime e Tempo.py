from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#criando uma data
lançamento_app = datetime(2021, 5, 28)
print(lançamento_app)
#quero receber uma data de lançamento do app.
#25/08/20
data_de_lançamento = datetime.strptime(input("Quando devemos lançar o app?"),'%d/%m/%Y')
print(type(data_de_lançamento))
print(data_de_lançamento)
#calcular o intervalo entre datas.
data_atual = datetime.now()
prazo = data_de_lançamento - data_atual
print(prazo.days)


