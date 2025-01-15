from math import isclose
from simple_calculator.calculator import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 3) == 2

def test_add_floats():
    assert isclose(add(0.1, 0.2), 0.3, rel_tol=1e-9)