from mal_types import Integer, Bolean, Nill

def pr_str(ast):
    if isinstance(ast, (Integer, Bolean, Nill)):
        return str(ast)
    if isinstance(ast, float):
        return str(ast)
    if isinstance(ast, str):
        return ast
    if isinstance(ast, list):
        out = str()
        out +="("
        for ind in range(len(ast)):
            if ind == len(ast)-1:
                out += pr_str(ast[ind])
            else:
                out += pr_str(ast[ind]) +" "
        out += ")"
        return out
