#Import relevant library
import random

#Create a list of items to shuffle
food = ["pizza", "burger", "salad", "steak"]

#Shuffle items
random.shuffle(food)

#Print results
for item in food:
    print(item)