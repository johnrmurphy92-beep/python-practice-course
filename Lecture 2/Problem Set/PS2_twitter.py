#Gather input from user
word = input("Enter a word please: ")

#Iterate over each letter in string
for letter in word:
    match letter:
        #Skip lowercase vowels without printing
        case "a" | "e" | "i" | "o" | "u":
            continue
        #Skip uppercase vowels without printing
        case "A" | "E" | "I" | "O" | "U":
            continue
        #Print all other letters in their original form
        case _:
            print(letter, sep="", end="")

 