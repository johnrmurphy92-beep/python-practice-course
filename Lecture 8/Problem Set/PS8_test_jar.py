#Import relevant function
from PS8_jar import Jar
import pytest

#Test initiation function
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-12)
    with pytest.raises(ValueError):
        Jar("Cat")

#Test string function
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

#Test deposit function
def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar = Jar(10)
    with pytest.raises(ValueError):        
        jar.deposit(20)

#Test withdraw function
def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
       jar.withdraw(8)