class Fizzbuzz:
    def __init__(self, n):
        result = []
        [result.append(str(i)) for i in range(1, n + 1)]
        self.list = result
        self.size = n

    def fizzbuzz(self, x, y):
        z = x + y
        for i in range(self.size):
            if ((i % z) == 0):
                self.list[i] = "FizzBuzz"

    def fizz(self, x):
        for i in range(self.size):
            if ((i % x) == 0):
                self.list[i] = "Fizz"

    def buzz(self, y):
        for i in range(self.size):
            if ((i % y) == 0):
                self.list[i] = "Buzz"