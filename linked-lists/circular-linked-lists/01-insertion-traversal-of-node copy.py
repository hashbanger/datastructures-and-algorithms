class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_empty(self, new_data):
        # if not empty return the head
        if self.head != None:
            return self.head
        
        # creating a new node
        new_node = Node(new_data)

        # creating connection
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node

        return self.head
    
    def insert_at_front(self, new_data):
        if self.head == None:
            return self.insert_in_empty(new_data)

        # creating and connecting
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = new_node

    def insert_at_end(self, new_data):
        if self.head == None:
            return serlf.insert_in_empty(new_data)

        # creating and connecting
        new_node = Node(new_data)
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, previous_node, new_data):
        # if None return None
        if self.head == None:
            return None
        
        ptr = self.head
        while ptr != None:
            # if node found, change connections
            if ptr.data == previous_node:
                new_node = Node(new_data)
                new_node.next = ptr.next
                ptr.next = new_node

                # if the node is also the last node
                # make new node the last node
                if ptr == self.tail:
                    self.tail = new_node
                    return
                else:
                    return

            # if it circles back, node not found
            if ptr.next == self.head:
                print(previous_node, " not present in the list")
                break

            ptr = ptr.next

    def print_list(self):
        if self.head is None:
            print("Empty List")
            return None
            
        ptr = self.head
        while True:
            print(ptr.data, end = ' - ')
            if ptr.next == self.head:
                print()
                break
            ptr = ptr.next

if __name__ == '__main__':
    llist = LinkedList()
    # inserting 5 as the head
    llist.insert_in_empty(5)
    # # inserting 3 before 5
    llist.insert_at_front(3)
    # # inserting 2 before 3
    llist.insert_at_front(2)
    # inserting 6 at the end
    llist.insert_at_end(6)
    # inserting 4 after 3
    llist.insert_after(3, 4)
    # inserting 7 after 6
    llist.insert_after(6, 7)
    # trying to insert 9 after a non-exiting node
    llist.insert_after(8, 9)
    # traversing the list
    llist.print_list()