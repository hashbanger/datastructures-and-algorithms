import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next

    def detect_and_remove_loop(self):
        # DETECTING THE LOOP
        slow_ptr = self.head
        fast_ptr = self.head
        # print(slow_ptr.data, fast_ptr.data)
        # if the slow and fast pointers are not null
        while (slow_ptr != None) and (fast_ptr != None) and (fast_ptr.next != None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            # if they are on the same node then there's a loop
            if slow_ptr.data == fast_ptr.data:
                # removing the loop
                self.remove_loop(slow_ptr)
                return

    def remove_loop(self, slow_ptr):
        current = self.head
        # we iterate over each node as current
        # and run the loop and see if it encounters the current
        while current:
            ptr = slow_ptr
            while ptr.next != slow_ptr and ptr.next != current:
                ptr = ptr.next

            if ptr.next == current:
                ptr.next = None
                return

            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(9)
    llist.insert_at_front(8)
    llist.insert_at_front(7)
    llist.insert_at_front(6)
    llist.insert_at_front(5)
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.head.next.next.next.next.next.next.next.next = llist.head.next.next
    print(llist.head.data, end=" - ")
    print(llist.head.next.data, end=" - ")
    print(llist.head.next.next.data, end=" - ")
    print(llist.head.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.data)

    slow = llist.detect_and_remove_loop()
    # llist.remove_loop(slow)
    llist.print_list()
