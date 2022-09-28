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

    # reversing the sublists in linked list
    def reverse_in_groups(self, head, group_size):
        if head is None:
            return None
        current = head
        prev_node = None
        next_node = None
        count = 0
        while (current != None) and (count < group_size):
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
            count += 1

        if next_node is not None:
            head.next = self.reverse_in_groups(next_node, group_size)

        return prev_node


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(24)
    llist.insert_at_front(15)
    llist.insert_at_front(10)
    llist.insert_at_front(29)
    llist.insert_at_front(20)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    print("Before Sub-Reverse: ")
    llist.print_list()
    llist.head = llist.reverse_in_groups(llist.head, 2)
    print("\nAfter Sub-Reverse: ")
    llist.print_list()
