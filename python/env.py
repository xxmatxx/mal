from mal_types import MalException

class Env:
    def __init__(self):
        self.outer = None
        self.data = dict()

    def set(self, key,value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self
        elif self.outer:
            return self.outer.find(key)
        else:
            return None

    def get(self, key):
        env = self.find(key)
        if not env:
            raise MalException(str(key) + " symbol not found")
        else:
            return env.data[key]
