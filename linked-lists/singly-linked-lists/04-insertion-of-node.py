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

    # Function to insert after a given previous node
    def insert_after(self, previous_node, new_data):
        if previous_node is None:
            print("The given previous node must be in the Linked List.")
            return

        # creating a node with new data
        new_node = Node(new_data)
        # attaching the previous' next to the new node's next
        new_node.next = previous_node.next
        # making the next of previous node as new node
        previous_node.next = new_node

    # Function to insert a new node at the end of the list
    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        # If list is empty then make the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # iterate to the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # make the new node as the last node
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    # inserting 5 as the head
    llist.insert_at_end(5)
    # inserting 3 before 5
    llist.insert_at_front(3)
    # inserting 2 before 3
    llist.insert_at_front(2)
    # inserting 6 at the end
    llist.insert_at_end(6)
    # inserting 4 after 3
    llist.insert_after(llist.head.next, 4)
    # traversing the list
    llist.print_list()
