import logging

logging.basicConfig(level=logging.DEBUG,filename='login.log',filemode='a', 
                    format= '%(levelname)s - %(message)s - %(asctime)s')#setar o nível

try:
    email = input('Digite seu e-mail')
    senha = int(input('Digite sua senha bancária'))
    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro: 
    print('Digite apenas números')
    logging.warning(erro)