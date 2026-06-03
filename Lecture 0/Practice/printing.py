#Collect name from user
name = input("What's your name? ")

#Remove extra spaces and capitalize
name=name.strip().title()

#Greet user by name
print(f"Hello, {name}")