class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # printing the contents of the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next

if __name__ == '__main__':
    llist = LinkedList()

    firstNode = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)

    llist.head = firstNode
    llist.head.next = secondNode
    secondNode.next = thirdNode

    llist.print_list()