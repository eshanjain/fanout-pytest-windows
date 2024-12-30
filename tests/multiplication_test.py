from calculator.operations import multiply

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6

def test_multiply_by_zero():
    assert multiply(5, 0) == 0
