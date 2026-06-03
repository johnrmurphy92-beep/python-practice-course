#Create a main function
def main():
        name = input("What's your name? ")
        hello(name)

#Create a printing function
def hello(target="world"):
        print("Hello,", target)

#Call relevant functions
main()
