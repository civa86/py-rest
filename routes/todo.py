from flask import Blueprint, jsonify, request

import services.logger as logger
from services.database import db_session

from models.todo import Todo

todo_route = Blueprint('todo_route', __name__)

# ****************************************************
# Get Todo List
# ****************************************************


@todo_route.route('/todo')
def listing():
    return jsonify([i.serialize for i in Todo.query.all()])

# ****************************************************
# Find Todo by ID
# ****************************************************


@todo_route.route('/todo/<int:id>')
def find(id):
    todo = Todo.query.filter(Todo.id == id).first()

    if todo is None:
        return jsonify({'error': 'Item Not Found'}), 404

    return jsonify(todo.serialize)

# ****************************************************
# Create new Todo
# ****************************************************


@todo_route.route('/todo', methods=['POST'])
def create():
    if request.json is None:
        return jsonify({'error': 'Missing Request Body'}), 400

    task = request.json.get('task')
    if not task:
        return jsonify({'error': 'Missing Task'}), 400

    todo = Todo(task)
    db_session.add(todo)
    db_session.commit()

    return jsonify(todo.serialize)

# ****************************************************
# Update a Todo
# ****************************************************


@todo_route.route('/todo/<int:id>', methods=['PUT'])
def update(id):
    if request.json is None:
        return jsonify({'error': 'Missing Request Body'}), 400

    todo = Todo.query.filter(Todo.id == id).first()

    if todo is None:
        return jsonify({'error': 'Item Not Found'}), 404

    task = request.json.get('task')
    if not task is None:
        todo.task = task

    done = request.json.get('done')
    if not done is None:
        todo.done = done

    db_session.commit()
    return jsonify(todo.serialize)

# ****************************************************
# Delete a Todo
# ****************************************************


@todo_route.route('/todo/<int:id>', methods=['DELETE'])
def delete(id):
    todo = Todo.query.filter(Todo.id == id).first()

    if todo is None:
        return jsonify({'error': 'Item Not Found'}), 404

    db_session.delete(todo)
    db_session.commit()

    return jsonify(todo.serialize)
