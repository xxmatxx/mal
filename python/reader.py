import re
from mal_types import MalException, Integer, Nill, Bolean, Symbol


class Reader:
    def __init__(self, tokens):
        self.data: list = tokens
        self.position: int = 0

    def next(self):
        if len(self.data) > self.position:
            self.position += 1
            return self.data[self.position-1]
        else:
            return None

    def peek(self):
        if len(self.data) > self.position:
            return self.data[self.position]


def tokenize(source: str):
    #vynechat komentaře
    tre = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""")
    return re.findall(tre, source)


def read_str(source):
    tokens = tokenize(source)
    reader = Reader(tokens)
    return read_form(reader)


def read_form(tokens: Reader):
    token = tokens.peek()
    if token == "(":
        return read_list(tokens)
    else:
        return read_atom(tokens)


def read_list(tokens: Reader):
    out = list()
    tokens.next()
    while(tokens.peek() != ")" and tokens.peek() is not None):
        out.append(read_form(tokens))
        tokens.next()
    if tokens.peek() is None:
        raise MalException("missing )")
    return out


def read_atom(tokens: Reader):
    token = tokens.peek()
    int_re = re.compile(r"-?[0-9]+$")
    float_re = re.compile(r"-?[0-9][0-9.]*$")
    if re.match(int_re, token):     return Integer(int(token))
    if re.match(float_re, token):   return float(token)
    if token == "true":             return Bolean(True)
    if token == "false":            return Bolean(False)
    if token == "nill":             return Nill()

    return Symbol(token)
