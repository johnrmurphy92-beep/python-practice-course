#Import relevant libraries
import re
import sys

#Define main function
def main():
    print(validate(input("IPv4 Address: ").strip()))

#Define function for validating input
def validate(ip):
    matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if matches:
        g1 = matches.group(1)
        g2 = matches.group(2)
        g3 = matches.group(3)
        g4 = matches.group(4)
        for g in (g1, g2, g3, g4):
            if len(g) >1 and g.startswith("0"):
                return False
            else: 
                g1 = int(g1)
                g2 = int(g2)
                g3 = int(g3)
                g4 = int(g4)

                if all(0 <= g <= 255 for g in (g1, g2, g3, g4)):
                    return True
                else:
                    return False
    else:
        return False   
   

#Call main function
if __name__ == "__main__":
    main()

