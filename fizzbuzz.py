import time as t
from threading import Event
class FizzBuzz:
    event_list = []
    event_f = Event()
    event_list.append(event_f)
    event_b = Event()
    event_list.append(event_b)
    event_fb = Event()
    event_list.append(event_fb)
    event_n = Event()
    event_list.append(event_n)
    event_main = Event()

    def __init__(self, n):
        self.string_list = []
        self.size = n
        self.index = 0
        
    def fizzbuzz(self):
        print("fizzbuzz called, no action")
        while self.index < self.size:
            print("in fizzbuzz while, before wait")
            self.event_fb.wait()
            print("in fizzbuzz while, after wait, before action")
            if self.index < self.size:
                self.string_list.append("FizzBuzz")
                self.index += 1
            print("in fizzbuzz while, after wait, after action")
            self.event_fb.clear()
            self.event_main.set()
            print("main is set")
            print("in fizzbuzz while, after wait, after action and clear")
            

    def fizz(self):
        print("fizz called, no action")
        while self.index < self.size:
            print("in fizz while, before wait")
            self.event_f.wait()
            print("in fizz while, after wait, before action")
            if self.index < self.size:
                self.string_list.append("Fizz")
                self.index += 1
            print("in fizz while, after wait, after action")
            self.event_f.clear()
            self.event_main.set()
            print("main is set")
            print("in fizz while, after wait, after action and clear")
            

    def buzz(self):
        print("buzz called, no action")
        while self.index < self.size:
            print("in buzz while, before wait")
            self.event_b.wait()
            print("in buzz while, after wait, before action")
            if self.index < self.size:
                self.string_list.append("Buzz")
                self.index += 1
            print("in buzz while, after wait, after action")
            self.event_b.clear()
            self.event_main.set()
            print("main is set")
            print("in buzz while, after wait, after action and clear")
            

    def number(self):
        print("number called, no action")
        while self.index < self.size:
            print("in number while, before wait")
            self.event_n.wait()
            print("in number while, after wait, before action")
            if self.index < self.size:
                self.string_list.append(str(self.index + 1))
                self.index += 1
            print("in number while, after wait, after action")
            self.event_n.clear()
            self.event_main.set()
            print("main is set")
            print("in number while, after wait, after action and clear")
            
