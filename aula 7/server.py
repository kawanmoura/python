from flask import Flask, jsonify, request, render_template

# Criando aplicação em Flask!
app = Flask(__name__)

# GET -> buscar algo
@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo como estao voces"
    })



@app.route('/')
def home():
    return render_template('index.html')



# Lista de tarefas
tarefas = [
    { "id": 1, "titulo": "Estudar Python", "feito": False },
    { "id": 2, "titulo": "Ler a doc", "feito": True }
]

# GET -> lista de tarefas
@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)




# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

# http://localhost:5000/helloworld
# http://localhost:5000/tarefas
# http://localhost:5000/