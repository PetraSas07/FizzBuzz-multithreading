import time as t
class FizzBuzz:
    def __init__(self, n):
        self.string_list = []
        self.size = n
        
    @property
    def index(self):
        return len(self.string_list)
        

    def fizzbuzz(self, x, y):
        z = x * y
        for i in range(1, self.size + 1):
            if ((i % z) == 0):
                self.string_list.append("FizzBuzz")

    def fizz(self, x):
        for i in range(1, self.size + 1):
            if ((i % x) == 0):
                self.string_list.append("Fizz")

    def buzz(self, y):
        for i in range(1, self.size + 1):
            if ((i % y) == 0):
                self.string_list.append("Buzz")

    def number(self):
        for i in range(1, self.size + 1):
            self.string_list.append(str(i))
