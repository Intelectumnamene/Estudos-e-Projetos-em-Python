#Maneira de separar as execuções dos programas em diferentes fluxos e cada fluxo terá uma nova rota a seguir.

import webbrowser
import threading
import time

def extrair_dados_do_site(site):
    print('Estamos navegando até o site {}'.format(site))
    webbrowser.open_new(site)
    for i in range(1, 20):
        print('Processando dados - {}/9'.format(i))
        time.sleep(1)
    print('Finalizado extração dos dado do site.')    

def baixar_arquivos():
    for i in range(1,10):
        print('Baixando arquivos - {}/10'.format(i))
        time.sleep(1)
    print('Arquivos baixados')

nova_thread = threading.Thread(target=extrair_dados_do_site, args=('http://www.devaprender.com',),daemon=True)#daemon serve para dizer se Thread está rodando em segundo plano ou não.
nova_thread.start()#inicializar a thread com o método start
baixar_arquivos()
nova_thread.join()#função join finalizar todo o processo