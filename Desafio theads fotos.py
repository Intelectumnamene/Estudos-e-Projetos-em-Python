import webbrowser
import threading
import time

def baixar_fotos(site):
    print('Estamos baixando fotos no site {}'.format(site))

def navegar_ate_site(site):
    print('Estamos navegando até o site {}'.format(site))



nova_thread = threading.Thread(target=baixar_fotos, args=('https://www.facebook.com',),daemon=True)#daemon serve para dizer se Thread está rodando em segundo plano ou não.
nova_thread.start()#inicializar a thread com o método start
navegar_ate_site('https://www.facebook.com')
nova_thread.join()#função join finaliza todo o processo