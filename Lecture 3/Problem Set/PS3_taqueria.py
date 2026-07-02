#Define dictionary containing prices
taqueria_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#Create running total variable
total = 0.00

#Prompt customer for order
while True:
    try:
        order = input("What do you want? ").title()
        if order in taqueria_menu:            
            total = total + float(taqueria_menu[order])
            print(f"${total:.2f}")
        else:
            pass
    except EOFError:
        print("Order complete")
        break