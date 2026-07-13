#Import package for text manipulation
from pyfiglet import Figlet
figlet = Figlet()

#Import package for system interface
import sys

#Import package for randomization
import random

#Assess command line input
if len(sys.argv) == 1:
    text = input("Input: ")
    fonts = figlet.getFonts()
    figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(text))


#Assess command line input
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fonts = figlet.getFonts()
        if sys.argv[2] in fonts:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    
else:
    sys.exit("Invalid usage")