# o if __name__ == __main__: é útil para chamar funcionalidades dentro de um pacote onde o código é executado somente.
#ao chamar o arquivo diretamente.


from carro  import ligar_carro 
from moto import ligar_moto

ligar_carro()
ligar_moto()

if __name__ == '__main__':
    print('Ligar véculos')
    print('Estamos no arquivo {}'.format(__name__))


#aqui estamos em uma situação hipotética onde as funcionalidades dos arquivos carro e moto foram usadas
#dentro desta pasta. Entretanto só será utilizadas partes das funções. ligar carro() e Ligar moto().
#Vale lembrar que nos respectivos arquivos também terão if __name__ == '__main__': mas com outros códigos
# que não serão rodados dentro do arquivo onde chamo as funções emprestadas.  

# esse tipo de estrutura é muito utilizado para quando precisamos determinar o escopo do código,
# onde ele só ira funcionar se estiver rodando dentro 
# do arquivo e com as otimizações feitas para ele.

#estrutura utilizada geralmente dentro de um pacote ou módulo
