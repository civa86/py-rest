from flask import Flask, jsonify, Response, send_from_directory, request
import os

import config
import services.logger as logger

# API Routes
# import packages.routes.image as routes_image

ENV = os.getenv('FLASK_ENV', 'production')

app = Flask(__name__)

logger.set_log_level()


@app.route('/')
def root():
    return jsonify({
        'message': 'Root API'
    })


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'resources'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# @app.route('/version.txt')
# def version():
#     with open("version.txt") as version_file:
#         return Response(version_file.read(), mimetype='text/plain')

if ENV != 'development':
    @app.errorhandler(Exception)
    def all_exception_handler(error):
        return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
