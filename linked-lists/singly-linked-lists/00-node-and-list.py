# The Node Class
class Node:
    # a function to initialize the node object
    def __init__(self, data):
        self.data = data  # the assigned data
        self.next = None  # the next node

# The Linked List Class
class LinkedList:
    # Function to initialize the Linked List
    def __init__(self):
        self.head = None
