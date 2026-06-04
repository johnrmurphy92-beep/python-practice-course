#Manually print bricks
print("#")
print("#")
print("#")

#Print bricks using a simple for loop
for _ in range(3):
    print("&")

#Use functions to accomplish the same goal
def main():
    height = prompt()
    brick = charachter()
    column(height, brick)

def prompt():
    while True:
        n = int(input("Enter positive number of bricks: "))
        if n > 0:
            return n

def charachter():
    c = str(input("Enter the charachter you want to use as a brick: "))
    return c

def column(height, brick):
    for _ in range(height):
        print(brick)

def row (width, brick):
    print(brick * width)

main()

#Use functions to print a rectangle
def main1():
    x = column_height()
    y = row_length()
    z = brick_type()
    print_rectangle(x, y, z)

def column_height():
    while True:
        ch = int(input("Enter block height: "))
        if ch > 0:
            return ch

def row_length():
      while True:
        rl = int(input("Enter block width: "))
        if rl > 0:
            return rl

def brick_type():
    bt = str(input("Enter the charachter you want to use as a brick: "))
    return bt

def print_rectangle(height, length, brick):
    for h in range(height):
        print(brick * length)

main1()