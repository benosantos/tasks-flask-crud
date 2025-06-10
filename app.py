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
    return jsonify({'message': 'Nova tafera criada com sucesso', 'id': new_task.id})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                'tasks': task_list,
                'total_tasks': len(task_list)
             }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({'message': 'Nao foi possivel encontrar a atividade'}), 404


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None:
        return jsonify({'message': 'Nao foi possivel encontrar a atividade'}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    return jsonify({'message': 'Tarefa atualizada com sucesso'})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if not task:
       return jsonify({'message': 'Nao foi possivel encontrar a atividade'}), 404

    tasks.remove(task)
    return jsonify({'message': 'Tarefa deletada com sucesso'}) 
    


app.run(debug=True)