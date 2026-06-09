#Set amount owed to price of drink
r = 50

#Create loop to request coins from user
while r > 0:
    while True: 
        n = int(input("Insert coin, please: "))
        if n == 25 or n == 10 or n == 5:
            break
        else:
            print("Amount due:", r)
    r = r - n
    if r > 0:
        print("Amount due:", r)

#Display amount of change owed
print("Change owed:", abs(r))