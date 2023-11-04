import webbrowser
import threading
import time
import random
def extrair_precos(site,produto):
    print('Navegando até o site {} e pesquisando sobre {}'.format(site, produto))
    time.sleep(5)
    print('{} processado com sucesso'.format(produto))

threads = []
produtos = ['celular','monitor','fone de ouvido','alto-falante','computador']

for i in range(5):
    nova_thread = threading.Thread(target= extrair_precos, args=('https://www.mercadolivre.com', produtos[i]))
    threads.append(nova_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()