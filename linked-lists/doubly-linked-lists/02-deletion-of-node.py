# for garbage collection
import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, new_data):
        # creating new node
        new_node = Node(new_data)

        # creating connections
        new_node.next = self.head

        # if head is not none
        if self.head != None:
            self.head.prev = new_node
        
        # changing the head
        self.head = new_node
    
    def insert_at_end(self, new_data):
        # creating new node
        new_node = Node(new_data)

        # if head is not None
        if self.head is None:
            self.head = new_node
            return

        # iterating the last node
        ptr = self.head
        while (ptr.next != None):
            ptr = ptr.next

        ptr.next = new_node
        new_node.prev = ptr

    def delete_node(self, dele):
        ptr = self.head
        if ptr is None or dele is None:
            return

        # if the node to be deleted is the first node
        if ptr.data == dele:
            ptr.next.prev = None
            self.head = ptr.next
            return
        
        while ptr:
            # when we reach the deletion node
            if ptr.data == dele:
                # if the node to be deleted is the last node
                # changing the last connection
                if ptr.next == None:
                    ptr.prev.next = None
                # otherwise changing connections
                else:
                    ptr.next.prev = ptr.prev
                    ptr.prev.next = ptr.next
                return

            ptr = ptr.next

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end = ' - ')
            ptr = ptr.next
        print()

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    llist.insert_at_end(5)
    llist.insert_at_end(5.5)
    llist.insert_at_end(6)
    llist.insert_at_end(7)
    llist.insert_at_end(8)
    llist.insert_at_end(9)
    llist.print_list()
    llist.delete_node(1)
    llist.delete_node(5.5)
    llist.delete_node(9)
    llist.print_list()
