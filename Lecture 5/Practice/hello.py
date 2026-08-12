#Define main function
def main():
    name = input("What is your name? ")
    print(hello(name))

#Define supporting function
def hello(to="world"):
    return f"hello, {to}"

#Ensure main only runs when called
if __name__ == "__main__":
    main()

