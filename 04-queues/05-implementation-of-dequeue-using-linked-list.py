# implementation of dequeue using doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Dequeue:
    def __init__(self, size):
        self.size = size
        self.front = None
        self.rear = None
        self.count = 0

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def insert_at_front(self, item):
        new_node = Node(item)
        if self.is_full():
            print("Queue Overflow!")
            return
        elif self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

        self.count += 1

    def insert_at_end(self, item):
        new_node = Node(item)

        if self.is_full():
            print("Queue Overflow")
            return
        elif self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def delete_from_front(self):
        if self.is_empty():
            print("Queue Underflow!")
            return

        item = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        self.count -= 1
        return item

    def delete_from_rear(self):
        if self.is_empty():
            print("Queue Underflow!")
            return

        item = self.front
        self.rear = self.rear.prev

        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

        self.count -= 1
        return item

    def peek_all(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        temp = self.front
        while temp:
            print(temp.data, end="-")
            temp = temp.next
        print()


if __name__ == "__main__":
    dequeue = Dequeue(10)
    dequeue.insert_at_end(5)
    dequeue.insert_at_end(6)
    dequeue.insert_at_end(7)
    dequeue.insert_at_end(8)

    dequeue.insert_at_front(4)
    dequeue.insert_at_front(3)
    dequeue.insert_at_front(2)
    dequeue.insert_at_front(1)

    dequeue.peek_all()

    dequeue.delete_from_front()
    dequeue.delete_from_front()

    dequeue.delete_from_rear()
    dequeue.delete_from_rear()
    dequeue.delete_from_rear()

    dequeue.peek_all()

    dequeue.delete_from_rear()
    dequeue.delete_from_rear()
    dequeue.delete_from_rear()

    dequeue.peek_all()
