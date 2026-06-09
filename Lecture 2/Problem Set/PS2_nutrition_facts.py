#Collect fruit from user
fruit = input("Enter name of fruit: ")

#Convert fruit name to lowercase
fruit = fruit.title()

#Define a dictionary of fruits and calories
nutrition = {
    "Apple":            130,
    "Avocado":          50,
    "Banana":           110,
    "Cantaloupe":       50,
    "Grapefruit":       60,
    "Grapes":           90,
    "Honeydew Melon":   50,
    "Kiwifruit":        90,
    "Lemon":            15,
    "Lime":             20,
    "Nectarine":        60,
    "Orange":           80,
    "Peach":            60,
    "Pear":	            100,
    "Pineapple":        50,
    "Plums":            70,
    "Strawberries":     50,
    "Sweet Cherries":   100,
    "Tangerine":        50,
    "Watermelon":       80
}

#Print calories for specifiec fruit
if fruit in nutrition:
    print("Calories:", nutrition[fruit])
else:
    pass