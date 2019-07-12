from step2_eval import REP
from mal_types import MalException
import pytest


def testing_evaluation_of_arithmetic_operations():
    assert ("3" == REP("(+ 1 2)"))
    assert("11" == REP("(+ 5 (* 2 3))"))
    assert("8" == REP("(- (+ 5 (* 2 3)) 3)"))
    assert("2" == REP("(/ (- (+ 5 (* 2 3)) 3) 4)"))
    assert("1010" == REP("(/ (- (+ 515 (* 87 311)) 302) 27)"))
    assert("-18" == REP("(* -3 6)"))
    assert("-994" == REP("(/ (- (+ 515 (* -87 311)) 296) 27)"))

    with pytest.raises(MalException):
        REP("(abc 1 2 3)")


def testing_empty_list():
    assert ("()" == REP("()"))
