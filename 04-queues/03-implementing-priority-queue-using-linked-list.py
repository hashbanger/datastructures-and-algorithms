# implementing a priority queue using a linked list


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.front = None

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def enqueue(self, value, priority):
        new_node = Node(value, priority)

        # we insert the new node at its appropriate position in the list by priority comparision
        if self.is_full():
            print(f"Queue Overflow by {value}")
            return
        elif self.is_empty():
            self.front = new_node
        else:

            # if the priority is highest we insert it at the front
            if self.front.priority < new_node.priority:
                new_node.next = self.front
                self.front = new_node

            # otherwise we find the correct place
            else:
                temp = self.front
                while (temp.next != None) and (temp.next.priority > new_node.priority):
                    temp = temp.next

                # then insert the node there
                new_node.next = temp.next
                temp.next = new_node

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return
        item = self.front
        self.front = self.front.next

        return item

    def peek(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        return self.front

    def peek_all(self):
        temp = self.front
        while temp.next != None:
            print(f"({temp.data}, {temp.priority})", end="-")
            temp = temp.next
        print()


if __name__ == "__main__":
    pqueue = PriorityQueue(10)
    pqueue.enqueue(18, 4)
    pqueue.enqueue(11, 7)
    pqueue.enqueue(13, 8)
    pqueue.enqueue(15, 10)
    pqueue.enqueue(14, 9)
    pqueue.enqueue(19, 5)
    pqueue.enqueue(17, 3)
    pqueue.enqueue(20, 6)
    print(f"Front element: {pqueue.peek().data}")
    print(f"Dequeued {pqueue.dequeue().data}")
    print(f"Front element: {pqueue.peek().data}")
    print(f"Dequeued {pqueue.dequeue().data}")
    print(f"Front element: {pqueue.peek().data}")
    print(f"Dequeued {pqueue.dequeue().data}")
    print(f"Front element: {pqueue.peek().data}")
    pqueue.peek_all()
