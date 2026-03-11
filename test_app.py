# test_app.py

from app import a, b, add

def test_addition():
    assert add(a, b) == 10