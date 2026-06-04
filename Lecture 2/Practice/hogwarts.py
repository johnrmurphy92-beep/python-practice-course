#Create list of students
students = ["Hermione", "Harry", "Ron"]

#Use index values to print student names
print(students[0])
print(students[1])
print(students[2])

#Use a simple for loop to print student names
for student in students:
    print(student)

#Use a simple for loop to print student names
for i in range(len(students)):
    print(i + 1, students[i])

#Create a dictionary with names and houses
people = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

#Use names to print houses
print(people["Hermione"])
print(people["Harry"])
print(people["Ron"])
print(people["Draco"])

#Use a simple for loop to print houses
for person in people:
    print(person, people[person],sep=": ")

#Create a list of dictionaries
youths = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None}
]

#Use a simple for loop to print relevant values
for youth in youths:
    print(youth["Name"], youth["House"], youth["Patronus"], sep=", ")