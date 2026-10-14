#Import relevant functions
from PS7_numb3rs import validate

#Define function to test numerical input
def test_letters():
    assert validate("AAA.AAA.AAA.AAA") == False
    assert validate("111.AAA.111.111") == False
    assert validate("1A1.A1A.1A1.A1A") == False
    assert validate("1$1.1$1.1$1.1$1") == False
    assert validate("111.111.111.111") == True

#Define function to test numerical number of characters
def test_length():
    assert validate("1111.1111.1111.1111") == False
    assert validate("111.111.111") == False
    assert validate("111.111.111.111.111") == False
    assert validate("111.111.111.111") == True

#Define function to test maginitude limitations
def test_magnitude():
    assert validate("276.276.276.276") == False
    assert validate("111.111.111.276") == False
    assert validate("000.000.000.000") == False
    assert validate("111.111.111.111") == True
    assert validate("255.255.255.255") == True
