from typing import Dict
from exceptions import ServerError
from app.models.scenery import Scenery
from app.models.server import Server
from app.models.user import User
from random import randint

scenery = Scenery()


def get_server_by_port(port):
    return scenery.get_server_by_port(port=port)


def create_server(data: Dict) -> Server:
    if data.get('name'):
        while True:
            port = randint(100000, 999999)
            if not scenery.if_server_exists(port):
                actual_server = scenery.adding_server(Server(port=port, users=[User(name=data['name'], admin=True)]))
                return actual_server
    else:
        raise ServerError()


def connect_server(data: Dict) -> Server:
    actual_server: Server = scenery.get_server_by_port(data['port'])
    actual_server.add_user_on_the_server(User(name=data['name']))
    return actual_server


def disconnect_server(data: Dict) -> scenery:
    actual_server: Server = scenery.get_server_by_port(data['port'])
    actual_server.remove_user_from_server(data['name'])
    return actual_server


def voted(data: Dict) -> Server:
    actual_server = scenery.get_server_by_port(data['port'])
    actual_server.user_voted_by_name(user_name=data['name'], voted_name=data['vote'])
    return actual_server


def ready_user(port: str, name: str) -> Server:
    actual_server = scenery.get_server_by_port(port=port)
    user = actual_server.get_user_by_name(name=name)
    user.change_ready()
    return actual_server


def started_votes(port: str) -> Server:
    actual_server = scenery.get_server_by_port(port)
    actual_server.start_server()
    return actual_server


def finish_votes(port: str) -> Server:
    actual_server = scenery.get_server_by_port(port)
    actual_server.finish_server()
    return actual_server
