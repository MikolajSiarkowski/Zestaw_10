class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return False

    def push(self, item):
        if len(self.items) >= 10:
            raise Exception('The stack is full!')
        else:
            self.items.append(item)         # dodajemy na koniec

    def pop(self):                      # zwraca element
        if self.is_empty == True:
            raise Exception('The stack is empty!')
        return self.items.pop()         # zabieram od końca



import unittest

class TestStackMethods(unittest.TestCase):

    def test_push(self):
        astack = Stack()
        with self.assertRaises(Exception):
            for i in range(11):
                astack.push(i)

    def test_pop(self):
        astack = Stack()
        with self.assertRaises(Exception):
            astack.pop()

    
if __name__ == '__main__':
    unittest.main()


