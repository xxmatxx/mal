from reader import read_str
from printer import pr_str


def READ(source):
    return read_str(source)


def EVAL(ast, env):
    return ast


def PRINT(exp):
    return pr_str(exp)


def REP(source):
    return PRINT(EVAL(READ(source), {}))


if __name__ == '__main__':
    header = "mal START"
    footer = "mal END"
    print(header)
    try:
        while True:
            data = input('>>')
            print(REP(data))
    except (EOFError, KeyboardInterrupt):
        pass
    print(footer)
