def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
#Initiate loop
    while True:

#Gather integer from user
        try:
            x = int(input("Enter x: "))

#Print error message if entered value isn't an integer
        except ValueError:
            print("The value of x provided is not an integer")

#Print the entered value
        else:
            break
    return(x)

main()    