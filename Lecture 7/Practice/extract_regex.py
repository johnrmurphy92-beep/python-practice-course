#Import regex library
import re

#Gather input from user
url = input("What is your Twitter URL? ").strip()

#Extract username from input
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))