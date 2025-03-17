from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de livros
livros = [
    {'id': 1, 'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'},
    {'id': 2, 'titulo': '1984', 'autor': 'George Orwell'},
    {'id': 3, 'titulo': 'O Hobbit', 'autor': 'J.R.R. Tolkien'}
]

# Rota para obter todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Rota para obter um livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = next((l for l in livros if l["id"] == id), None)
    if livro:
        return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Rota para editar um livro por ID (PUT)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for livro in livros:
        if livro['id'] == id:
            livro.update(livro_alterado)
            return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Rota para adicionar um novo livro (POST)
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1  # Gera ID automático
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
