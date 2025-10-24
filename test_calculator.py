import pytest
from calculator import add, subtract, multiply, divide, power, square_root

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0
def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2
    assert divide(0, 1) == 0
    assert divide(5, 0) == "Oops! Division by zero. X("
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-2, 2) == 4
def test_square_root():
    assert square_root(9) == 3
    assert square_root(0) == 0
    assert square_root(-4) == "Can't take the square root of a negative number. Duh."
def test_invalid_inputs():
    with pytest.raises(TypeError):
        add("a", 2)
    with pytest.raises(TypeError):
        subtract(5, "b")
    with pytest.raises(TypeError):
        multiply("x", "y")
    with pytest.raises(TypeError):
        divide(10, "z")
    with pytest.raises(TypeError):
        power("base", 2)
    with pytest.raises(TypeError):
        square_root("number")
def test_edge_cases():
    assert add(1e10, 1e10) == 2e10
    assert subtract(-1e10, -1e10) == 0
    assert multiply(1e5, 1e5) == 1e10
    assert divide(1e10, 1e5) == 1e5
    assert power(2, 100) == 1267650600228229401496703205376
    assert square_root(1e10) == 100000.0