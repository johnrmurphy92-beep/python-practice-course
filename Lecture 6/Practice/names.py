#Gather input from user
name = input("What's your name? ")

#Write results to file
with open("names.txt","a") as file:
    file.write(f"{name}\n")
