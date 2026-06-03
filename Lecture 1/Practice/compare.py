#Define input values
x = int(input("Define x "))
y = int(input("Define y "))

#Execute logical simple comparison
if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")

#Execute logical comparison with or operator
if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")