#Import function for testing
from PS5_bank import value

#Establish tests for $0 scenario
def test_zero():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello!") == 0

#Establish tests for $20 scenario
def test_twenty():
    assert value("Hey") == 20
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("Hey!") == 20

#Establish tests for $100 scenario
def test_hundred():
    assert value("Morning") == 100
    assert value("Well hello") == 100
    assert value("Oh hi") == 100
    assert value("Good afternoon") == 100
    assert value("1-1ello") == 100