#Import square function
from calculator import square

#Define main function
def main():
    test_square()

#Define test function
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("You've done fucked up")
    try:
        assert square(3) == 9
    except AssertionError:
        print("You've done fucked up")
    try:
        assert square(0) == 0
    except AssertionError:
        print("You've done fucked up")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("You've done fucked up")

    #Ensure main only runs when called
if __name__ == "__main__":
    main()