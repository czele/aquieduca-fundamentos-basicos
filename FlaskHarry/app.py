from flask import Flask
app = Flask(__name__)

app.config['TESTING'] = True

@app.route("/get", methods=['GET'])
def get():
    return 'Listado com sucesso!!!'

@app.route("/post", methods=['POST'])
def post():
    return 'Postado com sucesso'

@app.route("/put", methods=['PUT'])
def put():
    x=84/2
    return(str(x))

@app.route("/delete", methods=['DELETE'])
def delete():
    return('Este valor foi deletado')

@app.route("/<id>", methods=['GET'])
def getid(id):
    return f'ID: {id}'
