# Implementing k-number of queues in a single array with space efficient approach
# We implement this in a similar way as k-stacks in an array, only that we would keep track of front and rear as well
# and update front at every dequeue.
# watch this explanation https://www.youtube.com/watch?v=_gJ3to4RyeQ&t=5150s


class KQueues:
    def __init__(self, n_queues, size):
        self.size = size
        self.elements = [None] * self.size
        self.fronts = [-1] * n_queues
        self.rears = [-1] * n_queues
        self.nexts = list(range(1, self.size))
        self.nexts.append(-1)

        self.free = 0

    def is_empty(self, q_num):
        return self.fronts[q_num] == -1

    def is_full(self, q_num):
        return self.free == -1

    def enqueue(self, q_num, item):
        if self.is_full(q_num):
            return False

        # get the next free slot index
        next_free = self.nexts[self.free]
        if self.fronts[q_num] == -1:
            self.fronts[q_num] = self.rears[q_num] = self.free
        else:
            # connect the previous element to the new element spot
            self.nexts[self.rears[q_num]] = self.free

            # update the rear to current spot
            self.rears[q_num] = self.free

        # push the item
        self.elements[self.free] = item

        # to indicate the queue ends at that place
        self.nexts[self.rears[q_num]] = -1

        # update the free spot
        self.free = next_free

    def dequeue(self, q_num):
        if self.is_empty(q_num):
            return False

        front_idx = self.fronts[q_num]
        item = self.elements[front_idx]

        # update the front to next element
        self.fronts[q_num] = self.nexts[front_idx]

        # update the next of current front to free spot
        self.nexts[front_idx] = self.free

        # make current front as new free spot
        self.free = front_idx
        return item

    def peek(self, q_num):
        if self.is_empty(q_num):
            return False

        front = self.elements[self.fronts[q_num]]
        return front


if __name__ == "__main__":
    kqueue = KQueues(3, 8)
    kqueue.enqueue(0, 1)
    kqueue.enqueue(0, 2)
    kqueue.enqueue(0, 3)

    kqueue.peek(0)

    kqueue.enqueue(1, 4)
    kqueue.enqueue(1, 5)

    kqueue.peek(1)

    kqueue.enqueue(0, 6)

    kqueue.peek(0)

    kqueue.enqueue(2, 7)
    kqueue.enqueue(2, 8)

    kqueue.peek(2)

    kqueue.dequeue(0)
    kqueue.dequeue(0)

    kqueue.peek(0)

    kqueue.enqueue(0, 9)
    kqueue.enqueue(0, 10)

    kqueue.peek(0)

    kqueue.dequeue(0)
    kqueue.dequeue(0)

    kqueue.peek(0)
