#Define jar class
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
           raise ValueError("Capacity must be an integer") 
        if not capacity > 0:
            raise ValueError("Capacity must be greater than zero")
        self._capacity = capacity
        self._size = 0 
        
    def __str__(self):
        cookie = "🍪"
        total = self._size
        return cookie * total

    def deposit(self, n):
        total = self._size + n
        if total > self._capacity:
            raise ValueError("Too many cookies!")
        self._size = self._size + n

    def withdraw(self, n):
        total = self._size -n
        if total < 0:
            raise ValueError("Not enough cookies!")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

#Define main function
def main():
    capacity = int(input("Jar capacity: "))
    deposit = int(input("Cookies purchased: "))
    withdraw = int(input("Cookies consumed: "))
    jar = Jar(capacity)
    print(f"Initial balance: {jar.size}")
    jar.deposit(deposit)
    print(f"After purchase: {jar.size}")
    print(jar)
    jar.withdraw(withdraw)
    print(f"After eating: {jar.size}")
    print(jar)

#Call main function when appropriate
if __name__ == "__main__":
    main()