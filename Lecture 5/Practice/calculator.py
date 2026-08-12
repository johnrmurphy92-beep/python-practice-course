#Define main function
def main():
    x = input("What is x? ")
    print("The square of x is", square(x))

#Define supporting function
def square(n):
    return n*n

#Ensure main only runs when called
if __name__ == "__main__":
    main()