from nose.tools import assert_equals
from step1_read_print import REP

def testing_read_of_numbers():
    assert_equals("1", REP("1"))
    assert_equals("7", REP("7"))
    assert_equals("7", REP("7"))
    assert_equals("-123", REP("-123"))

def testing_read_of_symbols():
    assert_equals("+", REP("+"))
    assert_equals("abc", REP("\t abc"))
    assert_equals("abc5", REP("abc5"))
    assert_equals("abc-def", REP("abc-def"))

def testing_of_non_numbers_starting_with_dash():
    assert_equals("-", REP("-"))
    assert_equals("-abc", REP("-abc"))
    assert_equals("->>", REP("->>"))

def testing_read_of_lists():
    assert_equals("(+ 1 2)", REP("(+ 1 2)"))
    assert_equals("()", REP("()"))
    assert_equals("()", REP("( )"))
    assert_equals("(nil)", REP("(nil)"))
    assert_equals("((3 4))", REP("((3 4))"))
    assert_equals("(+ 1 (+ 2 3))", REP("(+ 1 (+ 2 3))"))
    assert_equals("(+ 1 (+ 2 3))", REP("( +   1   (+   2 3   )   )  "))
    assert_equals("(* 1 2)", REP("(* 1 2)"))
    assert_equals("(** 1 2)", REP("(** 1 2)"))
    assert_equals("(* -3 6)", REP("(* -3 6)"))

def test_commas_as_whitespace():
    assert_equals("(1 2 3)", REP("(1 2, 3,,,,),,"))
