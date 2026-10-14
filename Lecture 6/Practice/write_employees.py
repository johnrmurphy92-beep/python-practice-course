#Import relevant modules
import csv

#Prompt user for data
name = input("Enter employee name: ")
role = input("Enter employee role: ")

#Open employee data file
with open("employees.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name","role"])
    writer.writerow({"name": name, "role":role})