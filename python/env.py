from mal_types import MalException


class Env:
    def __init__(self, outer=None, binds=None, exprs=None):
        self.outer = outer
        self.data = dict()
        if binds:
            for i in range(len(binds)):
                self.set(binds[i],exprs[i])

    def set(self, key, value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self.data[key]
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
