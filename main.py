from flask import Flask, jsonify, send_from_directory
import os

import services.logger as logger
from services.database import db_session

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


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if ENV != 'development':
    @app.errorhandler(Exception)
    def all_exception_handler(error):
        return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
