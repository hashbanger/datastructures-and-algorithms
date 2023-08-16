# Implementing a highest priority first queue using an array
# We take the priority value min as the highest priority
# we enqueue them normally but while removing we peek the max priority element and remove it
# then shift all the remaining elements to overwrite the removed one.
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
            return False

        # increase the total counts and insert the element at the correct index
        item = Item(value, priority)
        self.count += 1
        self.elements[self.count - 1] = item

    def peek(self):
        max_priority = 999999  # dummy positive infinity
        max_idx = self.get_size()

        # we iterate to find the maximum element
        idx = 0
        while idx < self.get_size():
            current_item = self.elements[idx]

            # if the priority is greater (lesser number) we reassign the max_priority
            # if the priority is equal to current maximum then
            # we prioritize the one enqueued first
            if max_priority > current_item.priority:
                max_priority = current_item.priority
                max_idx = idx
            idx += 1

        return max_idx

    def dequeue(self):
        if self.is_empty():
            return False

        # fetching the details for the element to be removed
        item_idx = self.peek()
        item = self.elements[item_idx]

        # shifting elements from the right to overwrite the removed
        idx = item_idx
        while idx < (self.get_size() - 1):
            self.elements[idx] = self.elements[idx + 1]
            idx += 1

        self.count -= 1

        return item

    def peek_all(self):
        for item in self.elements:
            if item:
                print((item.value, item.priority), end="--")
        print()


if __name__ == "__main__":
    pqueue = PriorityQueue(10)
    pqueue.enqueue(41, 5)
    pqueue.enqueue(13, 4)
    pqueue.enqueue(32, 2)
    pqueue.enqueue(17, 1)
    pqueue.enqueue(99, 9)
    pqueue.enqueue(74, 8)
    pqueue.enqueue(21, 7)
    pqueue.enqueue(20, 6)

    pqueue.peek_all()

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")

    print(f"Dequeued {pqueue.dequeue().value}")

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")

    print(f"Dequeued {pqueue.dequeue().value}")

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")

    pqueue.enqueue(32, 0)

    print(f"Max Priority Element {pqueue.elements[pqueue.peek()].value}")
