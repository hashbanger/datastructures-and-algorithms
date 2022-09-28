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

    def reverse_list(self):
        previous_node = None
        next_node = None
        current_node = self.head
        while current_node != None:
            # store the next node
            next_node = current_node.next
            # revert the next of current node to previous
            current_node.next = previous_node
            # move the previous pointer to current
            previous_node = current_node
            # iterate to next
            current_node = next_node
        self.head = previous_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(7)
    llist.insert_at_front(6)
    llist.insert_at_front(5)
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    print("Before Reverse:")
    llist.print_list()
    llist.reverse_list()
    print("\nAfter Reverse:")
    llist.print_list()
