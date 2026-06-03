#Define main function
def main():
    x = float(input("What is x? "))
    y = float(input("What is y? "))
    print("The sum of squares for x and y ", square(x) + square(y))

#Define squaring function
def square(n):
    return n ** 2

#Execute main code
main()

