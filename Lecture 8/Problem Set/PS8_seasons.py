#Import relevant libraries
from datetime import date
import inflect
import sys

#Define main function
def main():
    raw = input("Date of birth: ").strip()
    try:
        start = formatter(raw)
    except ValueError:
        sys.exit("Invalid date")
    minutes = calculator(start)
    words = printer(minutes)
    print(f"{words} minutes")

#Define date formatter function
def formatter(raw):
    formatted = date.fromisoformat(raw)
    return formatted

#Define time calculator function
def calculator(start):
    end = date.today()
    duration = end - start
    days = duration.days
    minutes = days * 1440
    return minutes

#Define printer function
def printer(number):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    words = words.capitalize()
    return words

#Call main function when appropriate
if __name__ == "__main__":
    main()