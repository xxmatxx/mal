from env import Env
from mal_types import MalException, Closure, Integer,Symbol
from pytest import raises
from step4_if_fn_do import EVAL, READ

def test_env_simple():
    env = Env()
    env.data = {
        "a": 1,
        "b": 2
    }
    
    env.set("c",3)

    assert (1 == env.get("a"))
    assert (2 == env.get("b"))
    assert (3 == env.get("c"))

    assert (None == env.get("d"))

def test_env_simple_w_symbols():
    env = Env()
    env.set(Symbol("a"),3)

    assert (3 == env.get(Symbol("a")))

def test_env_init():
    env = Env(None,("a","b"), (1,2))

    env.set("c",3)

    assert (1 == env.get("a"))
    assert (2 == env.get("b"))
    assert (3 == env.get("c"))

    
    assert (None == env.get("d"))

def test_env_nested():
    outer = Env(None,("a","b"), (1,2))
    inner = Env(outer,("c","a"), (3,4))

    assert (4 == inner.get("a"))
    assert (2 == inner.get("b"))
    assert (3 == inner.get("c"))

    assert (inner == inner.find("a"))
    assert (outer == inner.find("b"))
    assert (inner == inner.find("c"))

    
    assert (None == inner.find("d"))

def test_env_nested_with_outer_empty():
    outer = Env()
    inner = Env(outer,("c","a"), (3,4))

    assert (4 == inner.get("a"))
    assert (3 == inner.get("c"))

    assert (inner == inner.find("a"))
    assert (inner == inner.find("c"))

    assert (None == inner.find("d"))

def test_env_from_closure():
    outer = Env(None,("a","b"), (1,2))
    closure = Closure(outer, ["a"], "a")
    envc = Env(closure.outer, closure.bind,[3])
    assert (3 == envc.get("a"))
    assert (3 == EVAL(READ(closure.ast),envc))
    
