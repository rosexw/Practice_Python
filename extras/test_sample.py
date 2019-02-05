#testing Python code using assert https://docs.python-guide.org/writing/tests/

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5