#Import CSV function library
import csv

#Create list to hold data
family = []

#Use CSV reader to parse data
with open("family.csv") as file:
    reader = csv.reader(file)
    for name, university in reader:
        family.append({"name": name, "university": university})

def get_name(member):
    return member["name"]

for member in sorted(family, key=get_name):
    print(f"{member['name']} went to {member['university']}!")

#Create new list to hold data
family_2 = []

#Use CSV dictionary reader to parse data
with open("family_header.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        family_2.append({"name": row["name"], "university": row["university"]})

def get_name(member):
    return member["name"]

for member in sorted(family_2, key=get_name):
    print(f"{member['name']} went to {member['university']}!")
