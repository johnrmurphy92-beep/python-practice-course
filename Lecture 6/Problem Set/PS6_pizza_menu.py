#Import relevant packages
from tabulate import tabulate
import csv
import sys

#Evaluate command line input
if len(sys.argv) == 2: 
    pass
else:
    sys.exit("Must enter exactly one command line argument")

#Extract path from command line
path = sys.argv[1]

#Validate provided path
if path.endswith(".csv"):
    pass
else: 
    sys.exit("Not a CSV file")

#Create empty list to hold contents
menu = []

#Read contents of CSV into a list of dictionaries
try:
    with open(path) as file:
        for line in file:
            pizza, small, large = line.rstrip().split(",")
            option = {}
            option["pizza"] = pizza
            option["small"] = small
            option["large"] = large
            menu.append(option)
except FileNotFoundError:
    sys.exit("File not found") 

#Pass results into table printing function
print(tabulate(menu, headers="firstrow",tablefmt="grid"))