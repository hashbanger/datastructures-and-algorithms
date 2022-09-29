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

        # we will iterate till we find the duplicate node and keep track of previous nodes
        # soon as we find the repeated node, we will connect the previous to null.
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

    # connecting the loop from node 11 to node 3
    llist.head.next.next.next.next.next.next.next.next.next.next.next = (
        llist.head.next.next
    )

    # not run into an infinite loop,
    # we would print the list like this.
    visited_nodes = set()
    current = llist.head
    while current.next != None:

        # checking if we have visited the nodes (! not by the data)
        if current in visited_nodes:
            print(current.data, end=" - ")
            print(f"Node {current.data} already visited! halting...")
            break

        print(current.data, end=" - ")
        visited_nodes.add(current)
        current = current.next

    # removing the loop
    slow = llist.detect_and_remove_loop()
    llist.print_list()
