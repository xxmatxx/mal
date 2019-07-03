def READ(source):
    return source


def EVAL(ast, env):
    return ast


def PRINT(exp):
    return exp


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
