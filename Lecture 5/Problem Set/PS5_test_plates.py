#Import relevant functions
from PS5_plates import is_valid

#Define function to test letters at beginning
def test_letters():
    assert is_valid("123456") == False
    assert is_valid("A12345") == False
    assert is_valid("AA1234") == True
    assert is_valid("AAA123") == True
    assert is_valid("AAAA12") == True
    assert is_valid("AAAAA1") == True
    assert is_valid("AAAAAA") == True

#Define function to test length requirements
def test_length():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAA") == True
    assert is_valid("AAAAA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") == False

#Define function to test number position
def test_placement():
    assert is_valid("AAA123") == True
    assert is_valid("AA123A") == False
    assert is_valid("AA123") == True
    assert is_valid("A123A") == False
    assert is_valid("AA120") == True
    assert is_valid("AA012") == False

#Define function to test punctuation
def test_punctuation():
    assert is_valid("AAA123") == True
    assert is_valid("AA-123") == False
    assert is_valid("AA 123") == False
    assert is_valid("AA123.") == False