#Collect name from user
name = input("What's your name? ")

#Return relevant house
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

elif name == "Draco":
    print("Slytherin")

else:
    print("Unrecognized name")

#Return relevant house using match
match name:
    case "Harry" | "Hermione" | "Ron":
       print("Gryffindor") 
    case "Draco":
         print("Slytherin")
    case _:
        print("Unrecognized name")

