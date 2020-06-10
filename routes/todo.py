from flask import Blueprint, jsonify, Response

import services.logger as logger
from models.todo import Todo

todo_route = Blueprint('todo_route', __name__)


@todo_route.route('/todo')
def todo_list():
    return jsonify(Todo.query.all())
