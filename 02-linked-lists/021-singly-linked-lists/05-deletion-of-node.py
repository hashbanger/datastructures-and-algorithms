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

    def delete_node(self, key):
        # store head node
        current = self.head

        # if head node itself holds the key to be deleted
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return
                
        # searching for the key to be deleted
        # tracking the previous of the key to be deleted as well
        while current is not None:
            if current.data == key:
                break
            previous = current
            current = current.next

        # if the key is not present in the linked list
        if current == None:
            return

        # Unlink the node from the linkedlist
        previous.next = current.next
        current = None

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
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    print("Before Deletion")
    llist.print_list()

    llist.delete_node(6)
    print("\nAfter Deletion")
    llist.print_list()
