from exceptions import ServerError
from app.models.user import User
from random import randint
from typing import List


class Server:
    def __init__(self, port: int = None, users: List[User] = None):
        if users is None:
            users = []

        if port is None:
            port = randint(100000, 999999)

        self.port = str(port)
        self._started = False
        self.users = users

    def get_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user

    def user_voted_by_name(self, user_name: str, voted_name: str):
        changed = False
        name_removed = None

        for user in self.users:
            if user.name == user_name:
                if user.vote == voted_name:
                    return user

                if not user.vote:
                    user.vote = voted_name
                    break

                if user.vote != voted_name:
                    changed = True
                    name_removed = user.vote
                    user.vote = voted_name
                    break

        for user in self.users:
            if changed:
                if user.name == name_removed:
                    user.number_of_votes -= 1

            if user.name == voted_name:
                user.number_of_votes += 1

    def add_user_on_the_server(self, user: User):
        if not self._started:
            if not self.if_name_exists_in_server(name=user.name):
                self.users.append(user)
        else:
            raise ServerError()

    def new_admin(self, index: int = None):
        if len(self.users) > 0:
            self.users[index].change_administrator_status()

    def remove_user_from_server(self, name: str):
        if self.if_name_exists_in_server(name=name):
            for user in self.users:
                if user.name == name:
                    self.users.remove(user)
                    if user.get_admin_status():
                        self.new_admin(0)
        raise ServerError()

    def start_server(self):
        for user in self.users:
            user.number_of_votes = 0
            user.vote = None
            if not user.get_ready():
                raise ServerError
        self._started = True
        return self._started

    def finish_server(self):
        self._started = False
        return self._started

    def if_name_exists_in_server(self, name: str) -> bool:
        for user in self.users:
            if user.name == name:
                return True
        return False

    def serialize(self):
        return {
            'port': self.port,
            'started': self._started,
            'users': [user.serialize() for user in self.users]
        }
