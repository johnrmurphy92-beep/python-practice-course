#Import relevant functions
from PS7_um import count

#Define function to test capitalization sensitivity
def test_case():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

#Define function to test use with punctuation and spaces
def test_punctuation():
    assert count("Um, hello") == 1
    assert count("Um what?") == 1
    assert count("Um?") == 1
    assert count("What is um your name?") == 1

#Define function to test false positives
def test_words():
    assert count("album") == 0
    assert count("mum") == 0
    assert count("umm") == 0
    assert count("Um, thanks, um, regular expressions make sense now") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    
    
    