
from step0_repl import REP


def testing_basic_string():
    assert("abcABC123" == REP("abcABC123"))


def testing_string_containing_spaces():
    assert("hello mal world" == REP("hello mal world"))


def testing_string_containing_symbols():
    assert("[]{}\"\'* ;:()" == REP("[]{}\"\'* ;:()"))


def testing_long_string():
    assert("hello world abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 (;:() []{}\"\'* ;:() []{}\"\'* ;:() []{}\"\'*)" == REP("hello world abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 (;:() []{}\"\'* ;:() []{}\"\'* ;:() []{}\"\'*)",))
