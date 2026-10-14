#Import regex library
import re

#Gather input from user
email = input("What's your email? ").strip()

#Use regular expressions to evaluate input
if re.search(r"^\w+@(\w+\.)?S\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")