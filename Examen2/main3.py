from flask import Flask, request, jsonify
from cliente2 import verificar_cliente

app = Flask(__name__)

@app.route('/cliente2', methods=['POST'])
def cliente():
    data = request.get_json()
    ci = data.get('ci')
    resultado = verificar_cliente(ci)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(port=5003)