#Import relevant functions
from PS8_seasons import formatter
from PS8_seasons import calculator
from PS8_seasons import printer
from datetime import date
import pytest

#Test formatter function
def test_formatter_valid():
    assert formatter("2025-10-04") == date(2025,10,4)
    assert formatter("1992-08-21") == date(1992,8,21)
    assert formatter("2000-01-01") == date(2000,1,1)

def test_formatter_invalid():
    with pytest.raises(ValueError):
        formatter("cat")
    with pytest.raises(ValueError):
            formatter("10/04/2025")
    with pytest.raises(ValueError):
            formatter("October 4th, 2025")

#Test calculator function
def test_calculator():
    assert calculator(date(2025,10,5)) == 525600 
    assert calculator(date(2024,10,5)) == 1051200

#Test printer function
def test_printer():
     assert printer(2) == "Two"
     assert printer(525600) == "Five hundred twenty-five thousand, six hundred"
     assert printer(1051200) == "One million, fifty-one thousand, two hundred"