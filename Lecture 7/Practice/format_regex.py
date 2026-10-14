#Import regex library
import re

#Gather input from user
name = input("What's your full name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    last = matches.group(1).strip()
    first = matches.group(2).strip()
    name = f"{first} {last}"
print(f"Hello, {name}.")