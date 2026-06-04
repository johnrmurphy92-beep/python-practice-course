#Gather expression from the user
expression = input("Enter expression: ")

#Remove leading or lagging whitespace
expression = expression.strip()

#Split expression into components
x, y, z = expression.split(" ")

#Convert numbers into integers
x = float(x)
z = float(z)

#Print values to confirm code is working
print(x)
print(y)
print(z)

#Execute requested operation
match y:
    case "+":
        print(round((x + z),1))
    case "-":
        print(round((x - z),1))
    case "*":
        print(round((x * z),1))
    case "/":
        print(round((x / z),1))