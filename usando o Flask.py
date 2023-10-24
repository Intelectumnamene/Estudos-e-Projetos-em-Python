# ### 1. Defnir o objetivo da API:

# Iremos montar uma api de músicas, onde deverá ser possível, consultar todas canções disponíveis, consultar uma canção individual, editar canções existentes e também excluir músicas existentes.

# ### 2. Qual será o URL base da API?

# Iremos utilizar o url base 'localhost'

# ### 3. Quais são os endpoints?

# Disponibilize endpoints para consultar, editar, criar e excluir

# ### 4. Quais recursos serão disponibilizados pela API?

# Informações sobre canções

# ### 5. Quais verbos http serão disponibilizados?

# * GET

# * POST

# * PUT

# * DELETE

# ### 6. Quais são os URLs completos para cada um?

# * GET http://localhost:5000/cancoes

# * GET http://localhost:5000/cancoes/1

# * POST http://localhost:5000/cancoes

# * PUT http://localhost:5000/cancoes/1

# * DELETE http://localhost:5000/cancoes/1

# ### 7. Qual deve ser a estrutura de cada canção

#  - lista de dicionários, que contem cancao e estilo

from flask import Flask, jsonify, request

app = Flask(__name__)
cancoes = [
    {
        'canção': 'Viver',
        'estilo': 'POP'
    },
    {
        'canção': 'Amar',
        'estilo': 'Rock',
    },
    {
        'canção': 'Pular',
        'estilo': 'Lambada'
    }
]

# Rota padrão - Get http://localhost:5000/
@app.route('/')
def obter_postagens():
    return jsonify(cancoes)

# Obter canção por id http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(cancoes[indice])

# Criar uma nova canção - Post - http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    cancoes.append(postagem)
    return jsonify(postagem), 200

# Alterar uma canção existente - Put - http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    cancoes[indice].update(postagem_alterada)
    return jsonify(cancoes[indice]), 200

# Excluir uma canção - Delete - http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    if indice < len(cancoes):
        del cancoes[indice]
        return jsonify({'message': 'A canção foi excluída com sucesso.'}), 200
    else:
        return jsonify({'message': 'Não foi possível encontrar a canção para exclusão.'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)

  
       