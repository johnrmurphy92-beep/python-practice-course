#Print text using a simple approach
print("meow")
print("meow")
print("meow")

#Print text using a basic while loop
n = 3
while n != 0:
    print("hiss")
    n = n - 1

#Print text using a basic while loop
n = 0
while n < 3:
    print("woof")
    n = n + 1

#Streamline syntax of optimal while loop
n = 0
while n < 3:
    print("hoot")
    n += 1

#Print text using a basic for loop
for i in [0, 1, 2]:
    print("roar")

#Print text using a basic for loop
for i in range(3):
    print("yowl")

#Streamline syntax of optimal for loop
for _ in range(3):
    print("yelp")

#Accomplish the same goal with text tools
print("bark\n" * 3, end="")

#Integrate user input into loop
while True:
    n = int(input("Please provide a positive value for n: "))
    if n > 0:
        break

for _ in range(n):
    print("howl")

#Generate a function capturing our code
def main():
    number = prompt()
    purr(number)


def prompt():
    while True:
        n = int(input("Please provide a positive value for n: "))
        if n > 0:
            return n  

def purr(n):
    for _ in range(n):
        print("purr")

main()