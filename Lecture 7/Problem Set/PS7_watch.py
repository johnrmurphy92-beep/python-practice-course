#Import relevant libraries
import re
import sys


#Define main function
def main():
    print(parse(input("HTML: ")))

#Define cleaning function
def parse(src):
    matches = re.search(r"^<iframe.*(?:src=)\"(?:https?://)?(?:www\.)?youtube\.com/embed/([a-z0-9]+).*</iframe>$", src,re.IGNORECASE)
    if matches:
        extension = (matches.group(1))
        base = "https://youtu.be/"
        return base + extension


#Call main function when needed
if __name__ == "__main__":
    main()