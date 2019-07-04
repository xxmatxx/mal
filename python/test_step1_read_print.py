from step1_read_print import REP

def testing_read_of_numbers():
    assert("1" == REP("1"))
    assert("7" == REP("7"))
    assert("7" == REP("7"))
    assert("-123" == REP("-123"))

def testing_read_of_symbols():
    assert("+" == REP("+"))
    assert("abc" == REP("\t abc"))
    assert("abc5" == REP("abc5"))
    assert("abc-def" == REP("abc-def"))

def testing_of_non_numbers_starting_with_dash():
    assert("-" == REP("-"))
    assert("-abc" == REP("-abc"))
    assert("->>" == REP("->>"))

def testing_read_of_lists():
    assert("(+ 1 2)" == REP("(+ 1 2)"))
    assert("()" == REP("()"))
    assert("()" == REP("( )"))
    assert("(nil)" == REP("(nil)"))
    assert("((3 4))" == REP("((3 4))"))
    assert("(+ 1 (+ 2 3))" == REP("(+ 1 (+ 2 3))"))
    assert("(+ 1 (+ 2 3))" == REP("( +   1   (+   2 3   )   )  "))
    assert("(* 1 2)" == REP("(* 1 2)"))
    assert("(** 1 2)" == REP("(** 1 2)"))
    assert("(* -3 6)" == REP("(* -3 6)"))

def test_commas_as_whitespace():
    assert("(1 2 3)" == REP("(1 2, 3,,,,),,"))
