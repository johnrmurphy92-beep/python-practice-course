#Define main function
def main():
    x = int(input("Define x "))
    if even_check(x):
        print("Even")
    else:
        print("Odd")

#Define function to check even status
def even_check(n):
     return (n % 2 == 0)

#Document less elegant way to achieve the same outcome
def even_check_alt1(n):
     return True if n % 2 == 0 else False

#Document least elegant way to achieve the same outcome
def even_check_alt2(n):
    if n % 2 == 0:
        return True
    else:
        return False

#Call main function
main()