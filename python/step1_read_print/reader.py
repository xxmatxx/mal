import re

class Reader:
    def __init__(self, tokens):
        self.data:list = tokens
        self.position:int = 0

    def next(self):
        self.position += 1
        return self.data[position-1]
    def peek(self):
        return self.data[position]


def tokenize(source:str):
    #vynechat komentaře
    tre = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""");
    return re.findall(tre, source)


def read_str(source):
    tokens = tokenize(source)
    reader = Reader(tokens)
    read_form(reader)


def read_form(tokens:Reader):
    if tokens.peek() == "(":
        tokens.next()
        read_list(tokens)
    else:
        read_atom(tokens)

def read_list(tokens:Reader):
    pass

def read_atom(tokens:Reader):
    pass
