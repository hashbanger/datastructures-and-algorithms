# Deletion of a node at a given position rather than a key
# Simple Method for Deletion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, position):
        # BEST CASE: O(1)
        # AVERAGE & WORST CASE: O(N) if positio given is size-1
        # SPACE COMPLEXITY: O(1) no extra any space is required
        if self.head is None:
            return
        
        if position == 0:
            self.head = self.head.next
            return self.head

        current_position = 0
        current = self.head
        while current is not None:
            if current_position == position:
                break
            previous_node = current
            current_position += 1
            current = current.next

        if current is None:
            return

        previous_node.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(6)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    print("Before Deletion")
    llist.print_list()

    llist.delete_node(1)
    print("\nAfter Deletion")
    llist.print_list()