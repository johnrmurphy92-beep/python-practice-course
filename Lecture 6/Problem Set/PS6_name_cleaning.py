#Import relevant libraries and modules
import csv
import sys

#Ensure appropriate number of command-line arguments provided
if len(sys.argv) == 3: 
    pass
elif len(sys.argv) < 3:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

#Extract paths from command line arguments and validate file type
path_input = sys.argv[1]
path_output = sys.argv[2]
if path_input.endswith(".csv") and path_output.endswith(".csv"):
    pass
else: 
    sys.exit("Both files must use CSV format")

#Read input CSV and save contents in a list of dictionaries for editing
roster = []
try:
    with open(path_input) as file:
        reader = csv.DictReader(file)
        for row in reader:
            roster.append({"name": row["name"], "house": row["house"]})
except FileNotFoundError:
    sys.exit("File not found")

#Split name entry into first and last name
for student in roster:
    student["last"], student["first"] = student["name"].split(",")
    student["first"] = student["first"].strip()

#Create a new list containing only the entries I want
roster_final = []
for student in roster:
    student_final = {
        "first": student["first"],
        "last": student["last"],
        "house": student["house"]
    }
    roster_final.append(student_final)

#Write resulting list into CSV file
with open(path_output, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(roster_final)