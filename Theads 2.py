import webbrowser
import  threading
import time
import random

def comentar(site,comentario):
    print('Entrando no site: {}'.format(site))
    print('Deixando um comentário {}'.format(comentario))
    time.sleep(5)
    print('Dados processados no site: {}'.format(site))

comentarios = ['oi','Olá','gostei', 'curti', 'muito bom']

threads = []
for site in range(100):
    nova_thread = threading.Thread(target=comentar, args=(site, random.choice(comentarios)))
    threads.append(nova_thread)

for thread in threads:
    thread.start()
    print('Iniciando {}'.format(thread.name))

for thread in threads:
    thread.join()
    print('Finalizando{}'.format(thread.name))