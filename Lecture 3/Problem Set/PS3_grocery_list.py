#Create empty dictionary to hold items
grocery_list = {}


#Prompt user for input
while True:
    try:    
        item = input("Enter list item: ").upper()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 1
    except EOFError:
        grocery_list_sorted = sorted(grocery_list)
        for item in grocery_list_sorted:
            print(grocery_list[item], item)
        break