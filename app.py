from flask import Flask, request
from models.task import Task

app = Flask(__name__)

# CRUD
# Create(Criar), Read(Ler), Update(Atualizar), Delete(Deletar)
# Tabela: Tarefa

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Tasks
    return 'Teste'


app.run(debug=True)