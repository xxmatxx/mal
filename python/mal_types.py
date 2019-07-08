class MalException(BaseException):
    pass

class Nill:
    def __init__(self):
        pass
    def __str__(self):
        return "nill"


class Bolean:
    def __init__(self,value):
        if value == True or value == False:
            self.value = value
        else:
            raise MalException("Wrong value " + str(value))

    def __str__(self):
        if self.value == True:      return "true"
        if self.value == False:     return "false"

    def __bool__():
        return self.value

class Integer:
    def __init__(self,value):
        if isinstance(value, int) and not isinstance(value, bool):
            self.value = value
        else:
            raise MalException("Wrong value " + str(value))

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return False

    def __add__(self, other):
        return Integer(self.value + other.value)

    def __sub__(self, other):
        return Integer(self.value - other.value)

    def __mul__(self, other):
        return Integer(self.value * other.value)

    def __truediv__(self, other):
        return Integer(self.value // other.value)


class Symbol():
    def __init__(self,value):
        if isinstance(value, str):
            self.value = value
        else:
            raise MalException("Wrong value " + value)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

class String(str):
    pass


class Function:
    pass

#list je list()
