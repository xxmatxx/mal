from nose.tools import assert_equals
from step0_repl import REP

def testing_basic_string():
    assert_equals("abcABC123",REP("abcABC123"))

def testing_string_containing_spaces():
    assert_equals("hello mal world",REP("hello mal world"))

def testing_string_containing_symbols():
    assert_equals("[]{}\"\'* ;:()",REP("[]{}\"\'* ;:()"))

def testing_long_string():
    assert_equals("hello world abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 (;:() []{}\"\'* ;:() []{}\"\'* ;:() []{}\"\'*)",
    REP("hello world abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 (;:() []{}\"\'* ;:() []{}\"\'* ;:() []{}\"\'*)",))
