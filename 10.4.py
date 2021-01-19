class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pusta
        return False

    def put(self, data):
        if len(self.items) >= 10:
            raise Exception('The queue is full!')
        self.items.append(data)

    def get(self): 
        if len(self.items) == 0:
            raise Exception('The queue is empty!')
        else:
            return self.items.pop(0)   # mało wydajne!


import unittest

class TestQueueMethods(unittest.TestCase):

    def test_push(self):
        aqueue = Queue()
        with self.assertRaises(Exception):
            for i in range(11):
                aqueue.put(i)

    def test_pop(self):
        aqueue = Queue()
        with self.assertRaises(Exception):
            aqueue.get()

    
if __name__ == '__main__':
    unittest.main()

