from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create(Criar), Read(Ler), Update(Atualizar), Delete(Deletar)
# Tabela: Tarefa

tasks = []
tasks_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global tasks_id_control
    data = request.get_json()
    new_task = Task(id=tasks_id_control, title=data['title'], description=data.get('description', ""))
    tasks_id_control += 1
    tasks.append(new_task)
    return jsonify({'message': 'Nova tafera criada com sucesso'})


app.run(debug=True)