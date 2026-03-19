import time as t
from threading import Event
class FizzBuzz:
    fizz = Event()
    buzz = Event()
    fizzbuzz = Event()

    def __init__(self, n):
        self.string_list = []
        self.size = n
        
    @property
    def index(self):
        return len(self.string_list)
        
    def fizzbuzz(cls, self):
        cls.fizzbuzz.wait()
        self.string_list.append("FizzBuzz")

    def fizz(cls, self):
        cls.fizz.wait()
        self.string_list.append("Fizz")

    def buzz(cls, self):
        cls.buzz.wait()
        self.string_list.append("Buzz")

    def number(cls, self, x, y):
        z = x * y
        for i in range(1, self.size + 1):
            if ((self.index + 1) % z) == 0:
                cls.fizzbuzz.set()
            elif ((self.index + 1) % x) == 0:
                cls.fizz.set()
            elif ((self.index + 1) % y) == 0:
                cls.buzz.set()
            else:
                self.string_list.append(str(i))
