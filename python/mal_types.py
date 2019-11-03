class MalException(BaseException):
    pass


class Nill:
    name = "Nill"

    def __init__(self):
        pass

    def __str__(self):
        return "nill"

    def __repr__(self):
        return "nill"


class Bolean:
    name = "Bolean"

    def __init__(self, value):
        if value is True or value is False:
            self.value = value
        else:
            raise MalException("Wrong value " + str(value))

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        if self.value is True:      return "true"
        if self.value is False:     return "false"

    def __repr__(self):
        if self.value is True:      return "true"
        if self.value is False:     return "false"

    def __bool__(self):
        return self.value
    
    def __hash__(self):
        return hash(self.value)


class Integer:
    name = "Integer"

    def __init__(self, value):
        if isinstance(value, int) and not isinstance(value, bool):
            self.value = value
        else:
            raise MalException("Wrong value " + str(value))

    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)

    def __bool__(self):
        return False

    def __eq__(self, other):
        return self.value == other

    def __hash__(self):
        return hash(self.value)

    def __add__(self, other):
        return Integer(self.value + other.value)

    def __sub__(self, other):
        return Integer(self.value - other.value)

    def __mul__(self, other):
        return Integer(self.value * other.value)

    def __truediv__(self, other):
        return Integer(self.value // other.value)


class Symbol():
    name = "Symbol"

    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise MalException("Wrong value " + value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other

class String(str):
    
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise MalException("Wrong value " + value)
    
    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)

class Key(str):
    
    def __init__(self, value):
        if isinstance(value, str):
            if value[0] == ":":
                self.value = value[1:]
            else:
                raise MalException("Wrong value " + value)
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __eq__(self, other):
        return self.value == other

class Closure:
    def __init__(self,env, bind, ast):
        self.outer = env
        self.bind = bind
        self.ast = ast
    def __str__(self):
        return "Closure"

    def __repr__(self):
        return "Closure"

#list je list()
"""
class List(list):
    pass

class Vector(list):
    pass

class Map(dict):
    pass
"""