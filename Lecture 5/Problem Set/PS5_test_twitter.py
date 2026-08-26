#Import relevant functions
from PS5_twitter import shorten

#Define function to test lowercase vowels
def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("goodbye") == "gdby"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("GOODBYE") == "GDBY"

def test_numbers():
    assert shorten("H3LL0") == "H3LL0"
    assert shorten("G00DBY3") == "G00DBY3"

def test_punctuation():
    assert shorten("Hello!") == "Hll!"
    assert shorten("Goodbye!") == "Gdby!"