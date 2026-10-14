#Import relevant libraries
import re
import sys

#Develop main function
def main():
    print(convert(input("Hours: ").strip()))

#Develop formatting function
def calculate(h,m,i):
    if i == "AM":
        if h == 12:
            return f"00:{m:02d}"
        else:
            return f"{h:02d}:{m:02d}"
    else:
        if h == 12:
            return f"{h:02d}:{m:02d}"
        else:
            return f"{h+12:02d}:{m:02d}"

#Develop validation function
def convert(standard):
    matches = re.search(r"^([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)$", standard)
    if matches:
        h1 = int(matches.group(1))
        m1 = int(matches.group(2) or 0)
        i1 = matches.group(3)
        h2 = int(matches.group(4))
        m2 = int(matches.group(5) or 0)
        i2 = matches.group(6)
    else:
        raise ValueError("Invalid input")

    if all(1 <= h <= 12 for h in (h1, h2)) and all(0 <= m <= 59 for m in (m1, m2)):
        start = calculate(h1,m1,i1)
        end = calculate(h2,m2,i2)
        return f"{start} to {end}"

    else:
        raise ValueError("Invalid input")


#Call main function when appropriate
if __name__ == "__main__":
    main()