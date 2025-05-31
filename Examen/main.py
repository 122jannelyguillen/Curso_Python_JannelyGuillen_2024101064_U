#!/usr/bin/env python3
from flask import Flask
from cliente import cliente

app = Flask(__name__)

# Registrar el blueprint de login
app.register_blueprint(cliente)

@app.route('/', methods=['POST'])
def hello():
    return 'ci'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)