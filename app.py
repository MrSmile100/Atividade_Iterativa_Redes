from flask import Flask, request, jsonify

app = Flask(__name__)

# dicionario simples para armazenar memória por enquanto
dados = {}

# Recebe dados via POST (JSON) e armazena no dicionário usando o "id" como chave
@app.route('/enviar', methods=['POST'])
def enviar():
    conteudo = request.json
    id_disp = conteudo.get("id")
    dados[id_disp] = conteudo
    return jsonify({"status": "ok"})

# Consulta os dados armazenados a partir de um "id" informado na URL
@app.route('/consultar/<id_disp>', methods=['GET'])
def consultar(id_disp):
    return jsonify(dados.get(id_disp, {}))

if __name__ == '__main__':
    app.run(debug=True)