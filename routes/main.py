from flask import Blueprint, jsonify, send_from_directory
import os

main_route = Blueprint('main_route', __name__)


@main_route.route('/')
def root():
    return jsonify({
        'message': 'Root API'
    })


@main_route.route('/favicon.ico')
def favicon():
    icon_dir = os.path.abspath(os.path.join(main_route.root_path, os.pardir, 'resources'))
    return send_from_directory(icon_dir, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @main_route.route('/version.txt')
# def version():
#     with open("version.txt") as version_file:
#         return Response(version_file.read(), mimetype='text/plain')
