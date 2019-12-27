from mal_types import Integer, Bolean, Nill, Symbol,Closure, String


def pr_str(ast):
    if isinstance(ast, (Integer, Bolean, Nill, Symbol,Closure, String)):
        return str(ast)
    elif isinstance(ast, float):
        return str(ast)
    elif isinstance(ast, str):
        return ast
    elif isinstance(ast, list):
        out = str()
        out += "("
        for ind in range(len(ast)):
            if ind == len(ast)-1:
                out += pr_str(ast[ind])
            else:
                out += pr_str(ast[ind]) + " "
        out += ")"
        return out
    else:
        raise BaseException("error printer.py")
