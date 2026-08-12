#Import relevant function
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    hello("David") == "hello, David"