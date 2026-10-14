#Create a student class
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

#Create a function that supplies print output
    def __str__(self):
        return f"{self.name} from {self.house}"

#Create getter functions
    @property
    def house(self):
        return self._house

    @property
    def name(self):
        return self._name

#Create setter functions
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @house.setter
    def house(self, house):
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self._house = house
    
#Define main function
def main():
    student = get_student()
    print(student)

#Define supporting function
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

#Call main function when needed
if __name__ == "__main__":
    main()