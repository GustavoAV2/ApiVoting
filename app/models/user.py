

class User:
    def __init__(self, name, admin=False):
        self.name = name
        self._admin = admin
        self._ready = False
        self.vote = None
        self.number_of_votes = 0

    def get_number_of_votes(self):
        return self.number_of_votes

    def get_ready(self):
        return self._ready

    def get_admin_status(self):
        return self._admin

    def voted(self, name):
        self.vote = name

    def adding_votes(self):
        self.number_of_votes += 1

    def removing_votes(self):
        self.number_of_votes -= 1

    def change_ready(self):
        self._ready = not self._ready

    def change_administrator_status(self):
        self._admin = not self._admin

    def serialize(self):
        return {
            'name': self.name,
            'admin': self._admin,
            'ready': self._ready,
            'vote': self.vote,
            'number_of_votes': self.number_of_votes
        }
