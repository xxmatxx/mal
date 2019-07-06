import pytest

from step3_env import *
from mal_types import MalException
from env import Env


def testing_REPL_ENV():
    env = Env()
    env.data = {'+': lambda a,b: a+b,
                '-': lambda a,b: a-b,
                '*': lambda a,b: a*b,
                '/': lambda a,b: int(a/b)}

    assert ("3" == PRINT(EVAL(READ("(+ 1 2)"), env)))
    assert ("2" == PRINT(EVAL(READ("(/ (- (+ 5 (* 2 3)) 3) 4)"), env)))

def testing_def_e():
    env = Env()
    env.data = {'+': lambda a,b: a+b,
                '-': lambda a,b: a-b,
                '*': lambda a,b: a*b,
                '/': lambda a,b: int(a/b)}

    assert ("3" == PRINT(EVAL(READ("(def! x 3)"), env)))
    assert ("3" == PRINT(EVAL(READ("x"), env)))
    assert ("4" == PRINT(EVAL(READ("(def! x 4)"), env)))
    assert ("4" == PRINT(EVAL(READ("x"), env)))
    assert ("8" == PRINT(EVAL(READ("(def! y (+ 1 7))"), env)))
    assert ("8" == PRINT(EVAL(READ("y"), env)))

def testing_if_symbols_are_case_sensitive():
    env = Env()
    env.data = {'+': lambda a,b: a+b,
                '-': lambda a,b: a-b,
                '*': lambda a,b: a*b,
                '/': lambda a,b: int(a/b)}

    assert ("111" == PRINT(EVAL(READ("(def! mynum 111)"), env)))
    assert ("222" == PRINT(EVAL(READ("(def! MYNUM 222)"), env)))
    assert ("111" == PRINT(EVAL(READ("mynum"), env)))
    assert ("222" == PRINT(EVAL(READ("MYNUM"), env)))

def testing_let_a():
    env = Env()
    env.data = {'+': lambda a,b: a+b,
                '-': lambda a,b: a-b,
                '*': lambda a,b: a*b,
                '/': lambda a,b: int(a/b)}

    assert ("4" == PRINT(EVAL(READ("(def! x 4)"), env)))
    assert ("9" == PRINT(EVAL(READ("(let* (z 9) z)"), env)))
    assert ("9" == PRINT(EVAL(READ("(let* (x 9) x)"), env)))
    assert ("4" == PRINT(EVAL(READ("x"), env)))
    assert ("6" == PRINT(EVAL(READ("(let* (z (+ 2 3)) (+ 1 z))"), env)))
    assert ("12" == PRINT(EVAL(READ("(let* (p (+ 2 3) q (+ 2 p)) (+ p q))"), env)))
    assert ("7" == PRINT(EVAL(READ("(def! y (let* (z 7) z))"), env)))
    assert ("7" == PRINT(EVAL(READ("y"), env)))

def testing_outer_environment():
    env = Env()
    env.data = {'+': lambda a,b: a+b,
                '-': lambda a,b: a-b,
                '*': lambda a,b: a*b,
                '/': lambda a,b: int(a/b)}

    assert ("4" == PRINT(EVAL(READ("(def! a 4)"), env)))
    assert ("9" == PRINT(EVAL(READ("(let* (q 9) q)"), env)))
    assert ("4" == PRINT(EVAL(READ("(let* (q 9) a)"), env)))
    assert ("4" == PRINT(EVAL(READ("(let* (z 2) (let* (q 9) a))"), env)))
