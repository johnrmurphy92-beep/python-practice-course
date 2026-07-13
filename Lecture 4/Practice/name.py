#Import relevant library
import sys

#Check for short entries
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#Print results for correct entries
for name in sys.argv[1:-1]:
    print("Hello, my name is", name)
