from flask import Flask, jsonify, send_from_directory
import os

import config
import services.logger as logger

# API Routes
from routes.todo import todo_route
from routes.main import main_route

ENV = os.getenv('FLASK_ENV', 'production')

app = Flask(__name__)

# Register Routes
app.register_blueprint(main_route)
app.register_blueprint(todo_route)

# Set logging level
logger.set_log_level()


if ENV != 'development':
    @app.errorhandler(Exception)
    def all_exception_handler(error):
        return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
