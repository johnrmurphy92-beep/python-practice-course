#Gather input from the user
greeting = input("Please provide a greeting! ")

#Remove leading or lagging whitespace
greeting = greeting.strip()

#Standardize case of user-provided input
greeting = greeting.lower()

#Check first letter in string against criteria
full = greeting.find("hello")

#Check first letter in string against criteria
partial = greeting.find("h")

#Calculate prize based on responses
if full == 0:
    print("$0")

elif partial == 0:
    print("$20")

else:
    print("$100")
