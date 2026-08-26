#Define main function
def main():
    while True:
        fraction = input("Enter fuel remaining in the form of X/Y: ")
        try:
            result = convert(fraction)
            break
        except (ValueError, ZeroDivisionError): 
            pass
    reading = gauge(result)
    print(reading)

#Define conversion function
def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    percentage = (x/y) * 100
    if 0 <= percentage <= 100:
        return round(percentage)
    else:
        raise ValueError
 
#Define gauage function
def gauge(percentage):
    if percentage >= 99:
        output = "F"
    elif percentage <= 1:
        output = "E"
    else:
        output = f"{percentage}%"
    return output


#Call main function
if __name__ == "__main__":
    main()