class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.last = None

    # Function to insert a new node at the beginning
    def insert_in_empty(self, new_data):
        # if not empty return the last
        if self.last != None:
            return self.last

        # creating a new node
        new_node = Node(new_data)
        self.last = new_node

        # creating connections
        self.last.next = self.last
        return self.last
    
    def insert_at_front(self, new_data):
        # if None do empty insertion
        if self.last == None:
            return self.insert_in_empty(new_data)
        
        # creating and connecting
        new_node = Node(new_data)
        new_node.next = self.last.next
        self.last.next = new_node

        return self.last

    def insert_at_end(self, new_data):
        # if None do empty insertion
        if self.last == None:
            return self.insert_in_empty(new_data)
        
        # creating and connecting
        new_node = Node(new_data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def insert_after(self, previous_node, new_data):
        # if None return None
        if self.last == None:
            return None

        # start a pointer from the head
        ptr = self.last.next
        # keep traversing
        while ptr != None:

            # if node found, change connections
            if ptr.data == previous_node:
                new_node = Node(new_data)
                new_node.next = ptr.next
                ptr.next = new_node

                # if the node is also last node 
                # make new node the last node
                if ptr == self.last:
                    self.last = new_node
                    return self.last
                else:
                    return self.last

            ptr = ptr.next

            # if it circles back, node not found
            if ptr == self.last.next:
                print(previous_node, " not present in teh list")
                break

        new_node = Node(new_data)

    def print_list(self):
        head = self.last.next
        while True:
            print(head.data, end=" - ")
            head = head.next
            if head == self.last.next:
                print(head.data)
                break

if __name__ == '__main__':
    llist = LinkedList()
    # inserting 5 as the head
    llist.insert_in_empty(5)
    # inserting 3 before 5
    llist.insert_at_front(3)
    # # inserting 2 before 3
    llist.insert_at_front(2)
    # inserting 6 at the end
    llist.insert_at_end(7)
    # inserting 4 after 3
    llist.insert_after(3, 4)
    # inserting 6 after 5
    llist.insert_after(5, 6)
    # # traversing the list
    llist.print_list()