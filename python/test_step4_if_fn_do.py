from step4_if_fn_do import *
from mal_types import MalException
from env import Env
def testing_enviroment_and_user_defined_functions():
    env = Env()
    env.data = {
                '+': lambda a, b: a+b,
                '-': lambda a, b: a-b,
                '*': lambda a, b: a*b,
                '/': lambda a, b: a/b
                }

    assert ("3" == PRINT(EVAL(READ("(+ 1 2)"), env)))
    assert ("7" == PRINT(EVAL(READ("( (fn* (a b) (+ b a)) 3 4)"), env)))
    assert ("4" == PRINT(EVAL(READ("( (fn* () 4) )"), env)))
    assert ("8" == PRINT(EVAL(READ("( (fn* (f x) (f x)) (fn* (a) (+ 1 a)) 7)"), env)))


def testing_closures():
    env = Env()
    env.data = {
                '+': lambda a, b: a+b,
                '-': lambda a, b: a-b,
                '*': lambda a, b: a*b,
                '/': lambda a, b: a/b
                }

    assert ("12" == PRINT(EVAL(READ("( ( (fn* (a) (fn* (b) (+ a b))) 5) 7)"), env)))
    assert ("Closure" == PRINT(EVAL(READ("(def! gen-plus5 (fn* () (fn* (b) (+ 5 b))))"), env)))
    assert ("Closure" == PRINT(EVAL(READ("(def! plus5 (gen-plus5))"), env)))
    assert ("12" == PRINT(EVAL(READ("(plus5 7)"), env)))
    assert ("Closure" == PRINT(EVAL(READ("(def! gen-plusX (fn* (x) (fn* (b) (+ x b))))"), env)))
    assert ("Closure" == PRINT(EVAL(READ("(def! plus7 (gen-plusX 7))"), env)))
    assert ("15" == PRINT(EVAL(READ("(plus7 8)"), env)))
