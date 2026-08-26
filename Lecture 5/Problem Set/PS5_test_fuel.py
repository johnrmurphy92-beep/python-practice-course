#Import relevant functions
from PS5_fuel import convert
from PS5_fuel import gauge
import pytest

#Test convert's handling of appropriate values
def test_convert_normal():
    assert convert("2/3") == 67
    assert convert("1/2") == 50
    assert convert ("0/1") == 0
    assert convert("1/1") == 100

#Test convert's handling of innapropriate values
def test_convert_abnormal():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
            convert("A/B")

#Test gauge's handling of integers
def test_gauge_all():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"