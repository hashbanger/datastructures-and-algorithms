# printing the maximum for each of the subarrays using sliding window
import sys


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

    def insert_at_rear(self, item):
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

    def peek_front(self):
        if self.is_empty():
            print("Queue Underflow!")
            return

        return self.front.data

    def peek_rear(self):
        if self.is_empty():
            print("Queue Underflow!")
            return

        return self.rear.data

    def peek_all(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        temp = self.front
        while temp:
            print(temp.data, end="-")
            temp = temp.next
        print()


def get_max_subarray_brute(arr, window):

    # iterating over each of the points till last window_size-th point
    for i in range(len(arr) - window + 1):
        current_max = -sys.maxsize

        # iterate over all elements of the current window
        for j in range(i, i + window):

            # reassign maximum if greater
            if arr[j] > current_max:
                current_max = arr[j]

        print(f"Maximum {current_max}")


def get_max_subarray_queue(arr, window):
    dqueue = Dequeue(len(arr))

    # first we will queue the elements' indexes in sorted order
    for i in range(window):

        # remove the elements' indexes from the queue if smaller than current element
        while (not dqueue.is_empty()) and (arr[dqueue.peek_rear()] < arr[i]):
            dqueue.delete_from_rear()

        # insert the index of the current element
        dqueue.insert_at_rear(i)

    # now we iterate through the remaining elements each
    for j in range(window, len(arr)):

        # print the maximum for the previous window
        print(f"Maximum {arr[dqueue.peek_front()]}")

        # remove the elements from the front which are obsolete for the current window
        # i.e. more than [window] elements older than current index
        while (not dqueue.is_empty()) and (dqueue.peek_front() <= (j - window)):
            dqueue.delete_from_front()

        # remove the elements' index which are smaller than current element
        while (not dqueue.is_empty()) and (arr[dqueue.peek_rear()] < arr[j]):
            dqueue.delete_from_rear()

        # insert the index of the current element
        dqueue.insert_at_rear(j)

    print(f"Maximum {arr[dqueue.peek_front()]}")


if __name__ == "__main__":
    arr = [24, 29, 30, 38, 46, 54, 20, 66, 89, 95, 10]
    window = 3
    print(f"Input array {arr}, window size {window}")
    get_max_subarray_brute(arr, window)
    print()
    get_max_subarray_queue(arr, window)
