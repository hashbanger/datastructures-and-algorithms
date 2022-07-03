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

    # Finding the length of the list
    def get_length(self):
        list_length = 0
        current = self.head
        # iterate until the last node
        while current is not None:
            current = current.next
            list_length += 1
        return list_length

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(6)
    llist.insert_at_front(9)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    llist.print_list()
    print(f"\nLength of the List is {llist.get_length()}")
