# implementing a highest priority first queue using an array
import sys


class Item:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.elements = [None] * self.size

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def enqueue(self, value, priority):
        if self.is_full():
            print(f"Queue Overflow by {value}")
            return

        # increase the total counts and insert the element at the correct index
        item = Item(value, priority)
        self.count += 1
        self.elements[self.count - 1] = item

    def peek(self):
        max_priority = -sys.maxsize
        max_idx = -1

        # we iterate to find the maximum element
        idx = 0
        while idx < self.get_size():
            current_item = self.elements[idx]

            # if the priority is greater we reassign the max_priority
            # if the priority is equal to current maximum then
            # we prioritize the one enqueued first
            if max_priority < current_item.priority:
                max_priority = current_item.priority
                max_idx = idx
            idx += 1

        return max_idx

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        item_idx = self.peek()
        item = self.elements[item_idx]

        idx = item_idx
        while idx < (self.get_size() - 1):
            self.elements[idx] = self.elements[idx + 1]
            idx += 1

        self.count -= 1

        return item


if __name__ == "__main__":
    pqueue = PriorityQueue(5)
    pqueue.enqueue(17, 3)
    pqueue.enqueue(41, 5)
    pqueue.enqueue(13, 4)
    pqueue.enqueue(32, 5)
    pqueue.enqueue(99, 9)
    pqueue.enqueue(23, 10)

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")

    pqueue.dequeue()

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")

    pqueue.dequeue()

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")

    pqueue.enqueue(67, 10)
    pqueue.enqueue(24, 9)

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")
