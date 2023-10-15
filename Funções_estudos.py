def gerar_nome_completo(complete):
    nome = input("Digite seu nome: ")
    print('Bem_vido! {}. {}'.format(nome,complete))
  
gerar_nome_completo('É um prazer conhecê-lo!')


def calcular_valores(preço_produto, quantidade = 1 ):
    print(preço_produto * quantidade)
calcular_valores(10,2)

def exibir_cotação_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)
exibir_cotação_do_dia('usd')

def obter_cotação_do_dia(moeda):
    if moeda == 'usd':
        return 5.47
    
cotaçao = obter_cotação_do_dia('usd')
if cotaçao > 5 :
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')