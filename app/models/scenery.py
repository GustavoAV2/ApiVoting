from app.models.server import Server
from exceptions import ServerError


class Scenery:
    def __init__(self):
        self.servers = []

    def adding_server(self, server: Server) -> Server:
        self.servers.append(server)
        return server

    def if_server_exists(self, port: str) -> bool:
        for server in self.servers:
            if server.port == port:
                return True
        return False

    def get_server_by_port(self, port: str) -> Server:
        if self.if_server_exists(port=port):
            for server in self.servers:
                if server.port == port:
                    return server
        else:
            raise ServerError

    def serialize(self):
        return {
            'servers': [
                server.serialize() for server in self.servers
            ]
        }
