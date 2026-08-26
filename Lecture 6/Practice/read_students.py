#Read data from CSV and print
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}.")

#Read data from CSV and print after sorting
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}!")

for student in sorted(students):
    print(student)

#Use disctionary to improve sorting process
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}?")