#Import relevant libraries
import re
import sys

#Define main function
def main():
    print(count(input("Text: ")))

#Define counting function
def count(quote):
    matches = re.findall(r"\bum\b" ,quote,re.IGNORECASE)
    total = len(matches)
    return total

#Call main function in file
if __name__ == "__main__":
    main()