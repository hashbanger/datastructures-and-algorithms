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

    def sorted_insert(self, new_data):
        new_node = Node(new_data)
        ptr = self.head
        # case 1, if the list is empty
        if self.head is None:
            self.insert_in_empty(new_data)
        # case 2, if the value is less than head
        elif new_node.data <= ptr.data:
            while ptr.next != self.head:
                ptr = ptr.next
            new_node.next = self.head
            ptr.next = new_node
            self.head = new_node
        # case 3, locating the node before insert point
        else:
            while (ptr.next != self.head) and (ptr.next.data < new_node.data):
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node

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
    input_values = [12, 32, 44, 23, 5, 0, 11]
    print("Values to insert")
    print(input_values)
    llist = LinkedList()
    print("\nSorted Insert")
    for value in input_values:
        llist.sorted_insert(value)
    llist.print_list()