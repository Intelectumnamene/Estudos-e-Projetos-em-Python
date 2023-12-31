# Requests não é uma API do Python,
# mas sim uma biblioteca de terceiros que permite fazer requisições HTTP 
# de maneira mais fácil e conveniente. 
# Essa biblioteca simplifica o processo de envio de solicitações HTTP, 
# como fazer solicitações GET e POST para interagir com servidores da web.


import requests
from pprint import pprint # exibe de forma mais legível os resultados de uma api

#usando GEt
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint(resultado_get.json())

#Get com id
resultado_get_com_id = requests.get('https://jsonplaceholder.typicode.com/todos/2')
#pprint(resultado_get_com_id.json())

#Post - Criar um novo recurso
nova_tarefa = {'completed': False,
 'title': 'Lavar o carro',
 'userId': 1}

resultado_post = requests.post('https://jsonplaceholder.typicode.com/todos',nova_tarefa)
pprint(resultado_post.json())
tarefa_alterada = {'completed': False,
 'title': 'Lavar a moto',
 'userId': 1}
#PUT - ALterar recurso já existente
resultado_put = requests.put('https://jsonplaceholder.typicode.com/todos/2',tarefa_alterada)
pprint(resultado_put.json())

#Delete - Excluir recurso
resultado_delete = requests.delete('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())