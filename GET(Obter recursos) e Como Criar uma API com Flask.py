
# jsonify é uma função fornecida pelo framework Flask, que é comumente usado para 
#construir respostas HTTP com formato JSON em suas aplicações web. 
# Ela converte um objeto Python (geralmente um dicionário) em uma representação JSON e, 
# em seguida, o inclui na resposta HTTP que é enviada de volta ao cliente que fez a solicitação.
from flask import Flask,jsonify,request


app = Flask(__name__)
postagens = [
    {
        'título' : 'História',
        'autor' : 'Amanda Dias'
    },
    {
        'título' : 'Novo Dispositivo Sony',
        'autor' : 'Howard String',
    },
    {
        'título' : 'Lançamento do Ano',
        'autor' : 'Jeff Bezos'
    }
]

#Rota padrão -Get  http://localhost:5000/
@app.route('/')#barra quer dizer que estamos na rota padrão.
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# #Criar uma nova postagem -Post - http://localhost:5000/postagem
@app.route('/postagem',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem,200)


# #Alterar uma postagem existente -Put-http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    return jsonify(postagens[indice],200)
 #Excluir uma postagem- Delete -Put-http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['PUT'])
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify('Foi excluida a postagem {}'.format(postagens[indice]),200)
        
    except:
        return jsonify('Não foi possíverl encontrar a postagens para exclusão',404)
#rodar o servidor
app.run(port=5000,host='localhost',debug=True)
