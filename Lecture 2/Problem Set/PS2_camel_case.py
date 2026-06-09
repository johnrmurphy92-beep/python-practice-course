#Gather input from user
name = input("Enter a variable name in camel case: ")

#Iterate over each letter in string
for letter in name:
    if letter.isupper() == True:     
        print("_", letter.lower(), sep="", end="")
    else:
        print(letter, sep="", end="")