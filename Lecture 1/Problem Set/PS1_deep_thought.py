#Collect input from user
response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#Remove leading and lagging spaces
response = response.strip()

#Convert strings to lowercase
response = response.lower()

#Check cleaned input against desired response
if response == "42" or response == "forty-two" or response == "forty two":
    print("Yes")

else:
    print("No")