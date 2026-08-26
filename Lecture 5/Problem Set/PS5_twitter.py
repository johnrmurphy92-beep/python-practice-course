#Define main function
def main():
    word = input("Enter a word please: ")
    output = shorten(word)
    print(output)

#Define supporting function
def shorten(word):

    #Create a blank sting to capture results
    output = ""
    
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
                output = output + letter
    return output

#Call main function
if __name__ == "__main__":
    main()