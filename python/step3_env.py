from reader import read_str
from printer import pr_str
from mal_types import MalException, Symbol

from env import Env

repl_env = Env()
repl_env.data = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b
}


def READ(source):
    return read_str(source)


def EVAL(ast, env):
    if not isinstance(ast, list):
        return eval_ast(ast, env)
    if isinstance(ast, list) and len(ast) == 0:
        return []
    if isinstance(ast, list):
        if str(ast[0]) == "def!":
            value = EVAL(ast[2], env)
            env.set(str(ast[1]), value)
            return value
        if str(ast[0]) == "let*":
            new_env = Env()
            new_env.outer = env
            for i in range(0, len(ast[1]), 2):
                new_env.set(str(ast[1][i]), EVAL(ast[1][i+1], new_env))
            return EVAL(ast[2], new_env)
        else:
            eval_list = eval_ast(ast, env)
            function = eval_list[0]
            return function(*eval_list[1:])


def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        out = env.get(str(ast))
        if out is None:
            raise MalException("symbol not found")
        else:
            return out
    if isinstance(ast, list):
        if len(ast) > 0:
            out = list()
            for x in ast:
                out.append(EVAL(x, env))
            return out
        else:
            return []
    return ast


def PRINT(exp):
    return pr_str(exp)


def REP(source):
    return PRINT(EVAL(READ(source), repl_env))


if __name__ == '__main__':
    header = "mal START"
    footer = "mal END"
    print(header)
    try:
        while True:
            try:
                data = input('>>')
                print(REP(data))
            except MalException as m:
                print(str(m))
    except (EOFError, KeyboardInterrupt):
        pass
    print(footer)