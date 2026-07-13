#Import relevant packages
import random

#Establish main function
def main():
    while True:
        try:
            level = get_level()
            total = 0
            correct = 0
            while total < 10:
                x = generate_integer(level)
                y = generate_integer(level)
                solution = x + y
                response = int(input(f"{x} + {y} = "))
                if response == solution:
                    total = total + 1
                    correct = correct + 1
                else:
                    attempt = 1
                    total = total + 1
                    print("EEE")
                    while attempt < 3:
                        response = int(input(f"{x} + {y} = "))
                        if response == solution:                            
                            correct = correct + 1
                            break
                        else:
                            attempt = attempt + 1                    
                            print("EEE")
                    else:
                        print(f"{x} + {y} = {solution} ")                 
            print("Score: ", correct)
            break         
        except ValueError: 
            pass

#Establish level function
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            pass

#Establish integer generator function
def generate_integer(level):
    if level in [1, 2, 3]:
        if level == 1:
            output = random.randint(0,9)
            return output
        elif level == 2:
            output = random.randint(10,99)
            return output
        else:
            output = random.randint(100,999)
            return output
    else:
        raise ValueError
        
if __name__ == "__main__":
    main()