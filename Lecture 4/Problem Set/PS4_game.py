#Import relevant packages
import random
import sys

#Prompt user for an integer
while True:
    limit = input("Level: ")
    if limit.isdigit() == True:
        answer = random.randint(1, int(limit))
        while True:
            guess = input("Guess: ")
            if guess.isdigit() == True:
                if int(guess) <= 0:
                    pass
                elif int(guess) == answer:
                    sys.exit("Just right!")
                elif int(guess) > answer:
                    print("Too large!")
                else:
                    print("Too small!")
            else:
                pass
    else:
        pass