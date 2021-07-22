from flask import Flask, request
app = Flask(__name__)

@app.route("/amy", methods=['GET'])
def name():
    return "Amy"

@app.route("/camila", methods=['POST'])
def nome():
    return "Camila"

@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == 'GET':
        return "Teste 1"
    else:
        return "Teste 2"
