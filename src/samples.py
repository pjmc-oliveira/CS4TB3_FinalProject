'Sample using increment and decrement expressions'
import random

class Seeker:
    'Class to hold a list of items, and iterate through them using ++ --'
    def __init__(self, items):
        self.items = list(items)
        self.index = 0
    
    def __incr__(self):
        self.index = (self.index + 1) % len(self.items)
        return self.items[self.index]
    
    def __decr__(self):
        self.index = (self.index - 1) % len(self.items)
        return self.items[self.index]
    
    def __str__(self):
        return str(self.items[self.index])

def lookup(needle, haystack):
    seek = Seeker(haystack)

    while ++seek != needle:
        print(f'Looking for {needle}, found {seek}')

if __name__ == "__main__":
    h = range(10)
    n = random.choice(list(h))
    lookup(n, h)
