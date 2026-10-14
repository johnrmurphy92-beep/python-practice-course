#Import relevant packages
import random

#Create a hat class
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod   
    def sort(cls , name):
        print(name, "is in", random.choice(cls.houses))

#Create an instance of the hat class
Hat.sort("Harry")