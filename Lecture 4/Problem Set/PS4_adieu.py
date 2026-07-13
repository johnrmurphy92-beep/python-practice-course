#Import relevant packages
import inflect
p = inflect.engine()

#Create an empty list to hold names
names = []

#Capture names from user
while True:
    try:
        new = input("Name: ")
        names.append(new)
    except EOFError:
        output = p.join(names)
        print("Adieu, adieu, to", output)
        break