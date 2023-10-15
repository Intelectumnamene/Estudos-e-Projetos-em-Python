import logging

# tipos de logging
# debug - informando algo para os desenvolvedores
# info - Informar algo que está acontecendo no programa sem dizer que é um erro.
# Warning - Acontecendo algo possivelmente fora do esperando , entretanto, ainda não é um erro. Mas pode geral futuramente.
# error - Erro que aconteceu na aplicação.
# critical - Erro com consequências graves.
logging.basicConfig(level=logging.DEBUG,filename='app.log',filemode='a', format= '%(levelname)s - %(message)s')#setar o nível 
logging.debug('Loggin nível debug')
logging.info('Loggin nível info')
logging.warning('Loggin nível warning')
logging.error('Loggin nível error')
logging.critical('Loggin nível critical')