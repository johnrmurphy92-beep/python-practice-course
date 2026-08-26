#Open relevant file and iterate over lines
with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())

#Sort names prior to printing
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hey, {name}")

#Simplify sorting process
with open("names.txt", "r") as file:
    for line in sorted(file):
        print("Morning,", line.rstrip())