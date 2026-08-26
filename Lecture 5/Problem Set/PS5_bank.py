#Define main function
def main():
    greeting = input("Please provide a greeting! ")
    output = value(greeting)
    print(output)

#Define supporting function
def value(greeting):

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
        output = 0

    elif partial == 0:
        output = 20

    else:
        output = 100

    #Return output value
    return(output)

#Call main function
if __name__ == "__main__":
    main()