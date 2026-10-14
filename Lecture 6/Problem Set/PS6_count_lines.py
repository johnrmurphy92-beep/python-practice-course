#Import relevant modules
import sys

#Check length of command line input
if len(sys.argv) == 2: 
    pass
else:
    sys.exit("Must enter exactly one command line argument")

#Extract path from command line
path = sys.argv[1]

#Validate provided path
if path.endswith(".py"):
    pass
else: 
    sys.exit("Not a Python file")

#Initialize counter variable
total = 0 

#Open file at the specified path
try:
    with open(path) as file:
        for line in file:
            trimmed = line.lstrip()
            if line.isspace():
                continue
            elif trimmed.startswith("#"):
                continue
            else: total = total + 1
except FileNotFoundError:
    sys.exit("File not found")

#Output total line count
print("The file contains", total, "lines.")

