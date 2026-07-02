#Define main function
def main():
    result = fuel_calculator()
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(int(round(result,0)),"%",sep="")

#Define supporting function
def fuel_calculator():
    while True:

#Request fraction from the user
        fraction = input("Enter fuel remaining in the form of X/Y: ")

#Convert values into integers and divide them
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            decimal = (x/y) * 100
            if 0 <= decimal <= 100:
                return(decimal)
            else: pass
        except (ValueError, ZeroDivisionError): 
            pass

#Call main function
main()