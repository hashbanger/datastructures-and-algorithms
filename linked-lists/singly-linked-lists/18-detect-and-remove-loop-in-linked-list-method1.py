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

        current = self.head
        previous = None

        visited_nodes = set()
        while current is not None:
            if current in visited_nodes:
                previous.next = None
                return

            visited_nodes.add(current)

            previous = current
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(11)
    llist.insert_at_front(10)
    llist.insert_at_front(9)
    llist.insert_at_front(8)
    llist.insert_at_front(7)
    llist.insert_at_front(6)
    llist.insert_at_front(5)
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    llist.head.next.next.next.next.next.next.next.next.next.next.next = (
        llist.head.next.next
    )
    print(llist.head.data, end=" - ")
    print(llist.head.next.data, end=" - ")
    print(llist.head.next.next.data, end=" - ")
    print(llist.head.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.next.next.next.data)

    slow = llist.detect_and_remove_loop()
    llist.print_list()
