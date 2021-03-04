from flask import jsonify, request, Blueprint
from app.actions.actions_server import get_server_by_port, disconnect_server, connect_server, create_server, \
    finish_votes, ready_user, started_votes, voted

app_server = Blueprint('app.server', __name__)


@app_server.route('/get-server/<port>')
def send_server(port: str):
    return jsonify(get_server_by_port(port).serialize()), 200


@app_server.route('/create-server', methods=['POST'])
def create():
    data = request.get_json()
    actual_server = create_server(data)
    return jsonify(actual_server.serialize()), 201


@app_server.route('/connect-server', methods=['POST'])
def connect():
    data = request.get_json()
    actual_server = connect_server(data)
    return jsonify(actual_server.serialize()), 201


@app_server.route('/disconnect-server', methods=['POST'])
def disconnect():
    data = request.get_json()
    disconnect_server(data)
    return jsonify({'msg': "Disconnected!"}), 201


@app_server.route('/ready/<port>/<name>', methods=['POST'])
def user_ready(port: str, name: str):
    actual_server = ready_user(port, name)
    return jsonify(actual_server.serialize()), 201


@app_server.route('/vote-server', methods=['POST'])
def vote():
    data = request.get_json()
    actual_server = voted(data)
    return jsonify(actual_server.serialize()), 201


@app_server.route('/started-server/<port>', methods=['POST'])
def started_server(port: str):
    actual_server = started_votes(port)
    return jsonify(actual_server.serialize()), 200


@app_server.route('/finish-server/<port>', methods=['POST'])
def finish_server(port: str):
    actual_server = finish_votes(port)
    return jsonify(actual_server.serialize()), 200
