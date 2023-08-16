# Implementing a traditional double ended queue using circular array
# Then a pythonic implementation more useful for problem solving.
class TraditionalDequeue:
    def __init__(self, size):
        self.size = size
        self.elements = [None] * self.size
        self.front = -1
        self.rear = -1
        self.count = 0

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def insert_at_front(self, item):
        if self.is_full():
            return False

        if self.is_empty():
            self.rear = 0

        self.front -= 1

        # we move the front to the end of the array if it reaches negative index
        if self.front < 0:
            self.front = self.size - 1

        self.elements[self.front] = item
        self.count += 1

    def insert_at_rear(self, item):
        if self.is_full():
            return False

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.elements[self.rear] = item
        self.count += 1

    def delete_from_front(self):
        if self.is_empty():
            return False

        item = self.elements[self.front]

        self.front = (self.front + 1) % self.size
        self.count -= 1

        return item

    def delete_from_rear(self):
        if self.is_empty():
            return False

        item = self.elements[self.rear]

        self.rear -= 1

        # we move rear to the end of the array if it reaches negative index
        if self.rear < 0:
            self.rear = self.size - 1

        self.count -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            return False
        return self.elements[self.front]

    def peek_rear(self):
        if self.is_empty():
            return False
        return self.elements[self.rear]

class Dequeue:
    def __init__(self):
        self.count = 0
        self.elements = []

    def get_size(self):
        return self.count
    
    def is_empty(self):
        return not self.elements

    def insert_at_front(self, item):
        self.elements.insert(0, item)

    def insert_at_rear(self, item):
        self.elements.append(item)

    def delete_from_front(self):
        if not self.is_empty():
            self.elements.pop(0)
        return False

    def delete_from_rear(self):
        if not self.is_empty():
            self.elements.pop()
        return False

    def peek_front(self):
        if not self.is_empty():
            return self.elements[0]
        return False

    def peek_rear(self):
        if not self.is_empty():
            return self.elements[-1]
        return False

    def peek_all(self):
        if not self.is_empty():
            return self.elements
        return False

if __name__ == "__main__":
    print("Traditional Dequeue:")
    dequeue = TraditionalDequeue(5)
    dequeue.insert_at_rear(4)
    dequeue.insert_at_rear(2)
    dequeue.insert_at_rear(0)
    dequeue.insert_at_rear(1)
    dequeue.insert_at_rear(3)
    dequeue.insert_at_rear(5)
    
    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.delete_from_front()

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.insert_at_front(6)

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.delete_from_rear()

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.insert_at_rear(5)

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.delete_from_front()

    dequeue.peek_front()
    dequeue.peek_rear()

    print("\nDequeue:")
    dequeue = Dequeue()
    dequeue.insert_at_rear(4)
    dequeue.insert_at_rear(2)
    dequeue.insert_at_rear(0)
    dequeue.insert_at_rear(1)
    dequeue.insert_at_rear(3)
    dequeue.insert_at_rear(5)

    print(dequeue.peek_all())
    print(dequeue.peek_front())
    print(dequeue.peek_rear())

    dequeue.delete_from_front()

    print(dequeue.peek_all())
    print(dequeue.peek_front())
    print(dequeue.peek_rear())

    dequeue.insert_at_front(6)

    print(dequeue.peek_all())
    print(dequeue.peek_front())
    print(dequeue.peek_rear())

    dequeue.delete_from_rear()

    print(dequeue.peek_all())
    print(dequeue.peek_front())
    print(dequeue.peek_rear())

    dequeue.insert_at_rear(5)

    print(dequeue.peek_all())
    print(dequeue.peek_front())
    print(dequeue.peek_rear())

    dequeue.delete_from_front()

    print(dequeue.peek_all())
    print(dequeue.peek_front())
    print(dequeue.peek_rear())