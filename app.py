from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from database import task_list_collection
from bson.objectid import ObjectId  # Importar ObjectId para manejar IDs de MongoDB

app = Flask(__name__)

# Página principal: lista todas las tareas
@app.route('/')
def index():
    tasks = task_list_collection.find()  # Obtener todas las tareas de la colección 'task_list'
    return render_template('index.html', tasks=tasks)

# Ruta para agregar una nueva tarea
@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description', '')  # La descripción es opcional
    if title:
        # Insertar la nueva tarea en la colección 'task_list'
        task_list_collection.insert_one({"title": title, "description": description, "completed": False})
    return redirect(url_for('index'))

# Ruta para marcar una tarea como completada
@app.route('/complete_task/<task_id>')
def complete_task(task_id):
    # Corregir el nombre de la colección y usar ObjectId correctamente
    task_list_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": True}})
    return redirect(url_for('index'))

# Ruta para eliminar una tarea
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    # Corregir el nombre de la colección y usar ObjectId correctamente
    task_list_collection.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for('index'))

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=4000)  # Cambiar el puerto a 4000 o el que prefieras
